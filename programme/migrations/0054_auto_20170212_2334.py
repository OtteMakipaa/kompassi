# -*- coding: utf-8 -*-
# Generated by Django 1.9.9 on 2017-02-12 21:34


from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('programme', '0053_populate_tag_slug'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='tag',
            unique_together=set([('event', 'slug')]),
        ),
    ]
