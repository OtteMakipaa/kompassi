# Generated by Django 1.9.5 on 2016-05-05 19:33


import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("labour", "0026_merge"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="shift",
            options={"ordering": ("job", "start_time"), "verbose_name": "shift", "verbose_name_plural": "shifts"},
        ),
        migrations.AlterField(
            model_name="job",
            name="job_category",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="labour.JobCategory", verbose_name="job category"
            ),
        ),
        migrations.AlterField(
            model_name="job",
            name="title",
            field=models.CharField(max_length=63, verbose_name="job title"),
        ),
        migrations.AlterField(
            model_name="jobrequirement",
            name="end_time",
            field=models.DateTimeField(verbose_name="ending time"),
        ),
        migrations.AlterField(
            model_name="jobrequirement",
            name="job",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="requirements",
                to="labour.Job",
                verbose_name="job",
            ),
        ),
        migrations.AlterField(
            model_name="jobrequirement",
            name="start_time",
            field=models.DateTimeField(verbose_name="starting time"),
        ),
        migrations.AlterField(
            model_name="shift",
            name="job",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, related_name="shifts", to="labour.Job"
            ),
        ),
        migrations.AlterField(
            model_name="shift",
            name="notes",
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name="shift",
            name="signup",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, related_name="shifts", to="labour.Signup"
            ),
        ),
        migrations.AlterField(
            model_name="workperiod",
            name="description",
            field=models.CharField(max_length=63, verbose_name="description"),
        ),
        migrations.AlterField(
            model_name="workperiod",
            name="end_time",
            field=models.DateTimeField(blank=True, null=True, verbose_name="ending time"),
        ),
        migrations.AlterField(
            model_name="workperiod",
            name="event",
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to="core.Event", verbose_name="event"),
        ),
        migrations.AlterField(
            model_name="workperiod",
            name="start_time",
            field=models.DateTimeField(blank=True, null=True, verbose_name="starting time"),
        ),
    ]