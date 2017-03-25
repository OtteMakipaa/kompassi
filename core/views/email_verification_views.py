# encoding: utf-8

from django.conf import settings
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.db.models import Q
from django.shortcuts import render, get_object_or_404, redirect
from django.utils.timezone import now
from django.views.decorators.http import require_http_methods, require_safe

from ..models import (
    EmailVerificationError,
    EmailVerificationToken,
    Event,
    Organization,
    PasswordResetError,
    PasswordResetToken,
    Person,
)
from ..forms import (
    LoginForm,
    PasswordForm,
    PasswordResetForm,
    PasswordResetRequestForm,
    PersonForm,
    RegistrationForm,
)
from ..utils import (
    get_next,
    groups_of_n,
    initialize_form,
    next_redirect,
    url,
)
from ..helpers import person_required


EMAIL_VERIFICATION_ERROR_MESSAGES = dict(
    default='Sähköpostiosoitteen vahvistus epäonnistui. Tarkista koodi.',
    wrong_person=
        'Ole hyvä ja kirjaudu ulos ja uudestaan sisään sillä käyttäjällä, jonka '
        'sähköpostiosoitetta yrität vahvistaa, ja yritä sitten uudelleen.',
    code_not_valid='Tämä vahvistuslinkki on jo käytetty tai mitätöity.',
    email_changed=
        'Sähköpostiosoitteesi on muuttunut sitten vahvistuslinkin lähetyksen. '
        'Ole hyvä ja käytä uusinta saamaasi vahvistuslinkkiä.',
    already_verified='Sähköpostiosoitteesi on jo vahvistettu.',
)


@person_required
@require_safe
def core_email_verification_view(request, code):
    person = request.user.person

    try:
        person.verify_email(code)
    except EmailVerificationError as e:
        reason = e.args[0]
        error_message = EMAIL_VERIFICATION_ERROR_MESSAGES.get(reason,
            EMAIL_VERIFICATION_ERROR_MESSAGES['default']
        )
        messages.error(request, error_message)
    else:
        messages.success(request, 'Kiitos! Sähköpostiosoitteesi on nyt vahvistettu.')

    return redirect('core_frontpage_view')


@person_required
@require_http_methods(['GET', 'HEAD', 'POST'])
def core_email_verification_request_view(request):
    person = request.user.person

    if person.is_email_verified:
        messages.error(request, 'Sähköpostiosoitteesi on jo vahvistettu.')
        return redirect('core_profile_view')

    if request.method == 'POST':
        person.setup_email_verification(request)
        messages.info(request,
            'Sinulle lähetettiin uusi vahvistuslinkki. Ole hyvä ja tarkista sähköpostisi.'
        )

    vars = dict(
        code=person.pending_email_verification,
    )

    return render(request, 'core_email_verification_request_view.jade', vars)


def remind_email_verification_if_needed(request, next=None):
    try:
        person = request.user.person
    except Person.DoesNotExist:
        return

    if person.is_email_verified:
        return
    elif next and next.startswith('/profile/email/verify'): # XXX hardcoded url fragment
        return
    elif person.pending_email_verification:
        messages.warning(request,
            'Muistathan vahvistaa sähköpostiosoitteesi! Sinulle on lähetetty vahvistusviesti '
            'sähköpostiisi. Jos viesti ei ole tullut perille, voit myös <a href="{}">pyytää '
            'uuden vahvistusviestin</a>.'.format(url('core_email_verification_request_view'))
        )
    else:
        messages.warning(request,
            'Pyydämme kaikkia käyttäjiämme vahvistamaan sähköpostiosoitteensa. Jotkin '
            '{settings.KOMPASSI_INSTALLATION_NAME_GENITIVE} toiminnot edellyttävät vahvistettua '
            'sähköpostiosoitetta. Saat vahvistuslinkin sähköpostiisi '
            '<a href="{request_page_url}">vahvistussivulta</a>.'.format(
                request_page_url=url('core_email_verification_request_view'),
                settings=settings
            )
        )
