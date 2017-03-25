# encoding: utf-8



from django.contrib.auth.models import Group
from django.db import models
from django.utils.translation import ugettext_lazy as _

import requests

from core.models import GroupManagementMixin, Organization


class AccessOrganizationMeta(models.Model, GroupManagementMixin):
    organization = models.OneToOneField(Organization, primary_key=True, verbose_name=_('organization'))
    admin_group = models.ForeignKey(Group, verbose_name=_('administrator group'))

    def __str__(self):
        return self.organization.name if self.organization is not None else 'None'

    class Meta:
        verbose_name = _('access management settings')
        verbose_name = _('access management settings')

    def get_group(self, suffix):
        group_name = self.make_group_name(self.organization, suffix)
        return Group.objects.get(name=group_name)
