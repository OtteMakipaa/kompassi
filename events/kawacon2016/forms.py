# encoding: utf-8

from django import forms

from crispy_forms.layout import Layout, Fieldset

from core.utils import horizontal_form_helper, indented_without_label
from labour.forms import AlternativeFormMixin
from labour.models import Signup, JobCategory, WorkPeriod

from .models import SignupExtra


class SignupExtraForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(SignupExtraForm, self).__init__(*args, **kwargs)
        self.helper = horizontal_form_helper()
        self.helper.form_tag = False
        self.helper.layout = Layout(
            Fieldset(u'Lisätiedot',
                'shirt_size',
                'special_diet',
                'special_diet_other',
                'prior_experience',
                'free_text',
            )
        )


    class Meta:
        model = SignupExtra
        fields = (
            'shirt_size',
            'special_diet',
            'special_diet_other',
            'prior_experience',
            'free_text',
        )

        widgets = dict(
            special_diet=forms.CheckboxSelectMultiple,
        )


class OrganizerSignupForm(forms.ModelForm, AlternativeFormMixin):
    def __init__(self, *args, **kwargs):
        event = kwargs.pop('event')
        admin = kwargs.pop('admin')

        assert not admin

        super(OrganizerSignupForm, self).__init__(*args, **kwargs)

        self.helper = horizontal_form_helper()
        self.helper.form_tag = False
        self.helper.layout = Layout(
            Fieldset(u'Tehtävän tiedot',
                'job_title',
            ),
        )

        self.fields['job_title'].help_text = u"Mikä on tehtäväsi coniteassa?"

    class Meta:
        model = Signup
        fields = ('job_title',)

        widgets = dict(
            job_categories=forms.CheckboxSelectMultiple,
        )

    def get_excluded_m2m_field_defaults(self):
        return dict(
            job_categories=JobCategory.objects.filter(event__slug='kawacon2016', name='Conitea')
        )


class OrganizerSignupExtraForm(SignupExtraForm, AlternativeFormMixin):
    pass