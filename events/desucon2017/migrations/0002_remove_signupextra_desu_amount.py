# -*- coding: utf-8 -*-
# Generated by Django 1.9.9 on 2017-01-31 21:23


from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('desucon2017', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='signupextra',
            name='desu_amount',
        ),
    ]
