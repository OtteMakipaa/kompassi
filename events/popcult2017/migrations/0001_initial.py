# -*- coding: utf-8 -*-
# Generated by Django 1.9.12 on 2017-01-12 19:59


from django.db import migrations, models
import django.db.models.deletion
import labour.models.signup_extras


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('core', '0023_auto_20160704_2155'),
        ('enrollment', '0002_enrollmenteventmeta_override_enrollment_form_message'),
    ]

    operations = [
        migrations.CreateModel(
            name='SignupExtra',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_active', models.BooleanField(default=True)),
                ('want_certificate', models.BooleanField(default=False, verbose_name='Haluan todistuksen ty\xf6skentelyst\xe4ni Popcult Helsingiss\xe4')),
                ('special_diet_other', models.TextField(blank=True, help_text='Jos noudatat erikoisruokavaliota, jota ei ole yll\xe4 olevassa listassa, ilmoita se t\xe4ss\xe4. Tapahtuman j\xe4rjest\xe4j\xe4 pyrkii ottamaan erikoisruokavaliot huomioon, mutta kaikkia erikoisruokavalioita ei v\xe4ltt\xe4m\xe4tt\xe4 pystyt\xe4 j\xe4rjest\xe4m\xe4\xe4n.', verbose_name='Muu erikoisruokavalio')),
                ('y_u', models.TextField(blank=True, help_text='Miksi juuri sin\xe4 sopisit hakemaasi ty\xf6teht\xe4v\xe4\xe4n? Voit kertoa itsest\xe4si vapaamuotoisesti: harrastukset, koulutus, hullu-kissanainen/v\xe4hemm\xe4n-hullu-koiraihminen yms.', verbose_name='Miksi juuri sin\xe4?')),
                ('prior_experience', models.TextField(blank=True, help_text='Kerro aikaisemmasta ty\xf6kokemuksestasi tapahtuman ty\xf6voimana tai muusta kokemuksesta, josta koet olevan hy\xf6ty\xe4 haetussa/haetuissa ty\xf6teht\xe4viss\xe4.', verbose_name='Ty\xf6kokemus')),
                ('free_text', models.TextField(blank=True, help_text='T\xe4ss\xe4 kent\xe4ss\xe4 voit kertoa jotain mink\xe4 koet tarpeelliseksi, jota ei ole viel\xe4 mainittu.', verbose_name='Lis\xe4tietoja')),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='popcult2017_signup_extras', to='core.Event')),
                ('person', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='popcult2017_signup_extra', to='core.Person')),
                ('special_diet', models.ManyToManyField(blank=True, related_name='_signupextra_special_diet_+', to='enrollment.SpecialDiet', verbose_name='Erikoisruokavalio')),
            ],
            options={
                'abstract': False,
            },
            bases=(labour.models.signup_extras.SignupExtraMixin, models.Model),
        ),
    ]
