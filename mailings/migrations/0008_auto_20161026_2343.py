# -*- coding: utf-8 -*-
# Generated by Django 1.9.9 on 2016-10-26 20:43


from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mailings', '0007_recipientgroup_personnel_class'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='channel',
            field=models.CharField(choices=[('email', 'S\xe4hk\xf6posti'), ('sms', 'Tekstiviesti')], default='email', max_length=5, verbose_name='Kanava'),
        ),
        migrations.AlterField(
            model_name='recipientgroup',
            name='app_label',
            field=models.CharField(choices=[('labour', 'Ty\xf6voima')], max_length=63, verbose_name='Sovellus'),
        ),
        migrations.AlterField(
            model_name='recipientgroup',
            name='verbose_name',
            field=models.CharField(blank=True, default='', max_length=63, verbose_name='Nimi'),
        ),
    ]
