# -*- coding: utf-8 -*-
# Generated by Django 1.9.9 on 2016-09-07 18:27


from django.db import migrations, models


PROGRAMME_STATES_ACTIVE = ['idea', 'asked', 'offered', 'accepted', 'published']


def populate_programme_role_is_active(apps, schema_editor):
    ProgrammeRole = apps.get_model('programme', 'ProgrammeRole')

    for programme_role in ProgrammeRole.objects.all().select_related('programme'):
        programme_role.is_active = programme_role.programme.state in PROGRAMME_STATES_ACTIVE
        programme_role.save()


class Migration(migrations.Migration):

    dependencies = [
        ('programme', '0048_auto_20160813_1948'),
    ]

    operations = [
        migrations.AddField(
            model_name='programmerole',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
        migrations.RunPython(populate_programme_role_is_active, elidable=True),
    ]
