# Generated by Django 1.9.1 on 2016-01-31 22:50


from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("labour", "0016_auto_20160128_1805"),
    ]

    operations = [
        migrations.AlterField(
            model_name="personnelclass",
            name="app_label",
            field=models.CharField(blank=True, default="labour", max_length=63),
        ),
    ]