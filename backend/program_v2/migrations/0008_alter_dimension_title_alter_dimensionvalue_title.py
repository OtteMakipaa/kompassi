# Generated by Django 4.2.7 on 2023-11-26 09:18

from django.contrib.postgres.fields import HStoreField
from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("program_v2", "0007_programv2eventmeta_skip_offer_form_selection"),
    ]

    operations = [
        migrations.AlterField(
            model_name="dimension",
            name="title",
            field=HStoreField(blank=True),
        ),
        migrations.AlterField(
            model_name="dimensionvalue",
            name="title",
            field=HStoreField(blank=True),
        ),
    ]
