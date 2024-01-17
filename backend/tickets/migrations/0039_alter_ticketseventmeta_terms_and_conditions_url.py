# Generated by Django 5.0.1 on 2024-01-17 19:31

import django.contrib.postgres.fields.hstore
from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("tickets", "0038_autumn_cleaning"),
    ]

    operations = [
        migrations.AlterField(
            model_name="ticketseventmeta",
            name="terms_and_conditions_url",
            field=django.contrib.postgres.fields.hstore.HStoreField(blank=True, default=dict),
        ),
    ]
