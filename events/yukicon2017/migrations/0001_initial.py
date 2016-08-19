# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-08-15 19:00
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import labour.models.signup_extras


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('core', '0023_auto_20160704_2155'),
    ]

    operations = [
        migrations.CreateModel(
            name='EventDay',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=63)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='SignupExtra',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_active', models.BooleanField(default=True)),
                ('shift_type', models.CharField(choices=[('yksipitka', b'Yksi pitk\xc3\xa4 vuoro'), ('montalyhytta', b'Monta lyhyemp\xc3\xa4\xc3\xa4 vuoroa'), ('kaikkikay', b'Kumpi tahansa k\xc3\xa4y')], help_text='Haluatko tehd\xe4 yhden pitk\xe4n ty\xf6vuoron vaiko monta lyhyemp\xe4\xe4 vuoroa?', max_length=15, verbose_name='Toivottu ty\xf6vuoron pituus')),
                ('total_work', models.CharField(choices=[('8h', b'Minimi - 8 tuntia'), ('12h', b'10\xe2\x80\x9312 tuntia'), ('yli12h', b'Ty\xc3\xb6n Sankari! Yli 12 tuntia!')], help_text='Kuinka paljon haluat tehd\xe4 t\xf6it\xe4 yhteens\xe4 tapahtuman aikana? Useimmissa teht\xe4vist\xe4 minimi on kahdeksan tuntia, mutta joissain teht\xe4viss\xe4 se voi olla my\xf6s v\xe4hemm\xe4n (esim. majoitusvalvonta 6 h).', max_length=15, verbose_name='Toivottu kokonaisty\xf6m\xe4\xe4r\xe4')),
                ('want_certificate', models.BooleanField(default=False, verbose_name='Haluan todistuksen ty\xf6skentelyst\xe4ni Yukiconissa')),
                ('shirt_size', models.CharField(choices=[('NO_SHIRT', 'Ei paitaa'), ('XS', 'XS Unisex'), ('S', 'S Unisex'), ('M', 'M Unisex'), ('L', 'L Unisex'), ('XL', 'XL Unisex'), ('XXL', 'XXL Unisex'), ('LF_S', 'S Ladyfit'), ('LF_M', 'M Ladyfit'), ('LF_L', 'L Ladyfit')], help_text='Ajoissa ilmoittautuneet v\xe4nk\xe4rit saavat maksuttoman ty\xf6voimapaidan. Kokotaulukot: <a href="http://www.bc-collection.eu/uploads/sizes/TU004.jpg" target="_blank">unisex-paita</a>, <a href="http://www.bc-collection.eu/uploads/sizes/TW040.jpg" target="_blank">ladyfit-paita</a>', max_length=8, verbose_name='Paidan koko')),
                ('special_diet_other', models.TextField(blank=True, help_text='Jos noudatat erikoisruokavaliota, jota ei ole yll\xe4 olevassa listassa, ilmoita se t\xe4ss\xe4. Tapahtuman j\xe4rjest\xe4j\xe4 pyrkii ottamaan erikoisruokavaliot huomioon, mutta kaikkia erikoisruokavalioita ei v\xe4ltt\xe4m\xe4tt\xe4 pystyt\xe4 j\xe4rjest\xe4m\xe4\xe4n.', verbose_name='Muu erikoisruokavalio')),
                ('prior_experience', models.TextField(blank=True, help_text='Kerro t\xe4ss\xe4 kent\xe4ss\xe4, jos sinulla on aiempaa kokemusta vastaavista teht\xe4vist\xe4 tai muuta sellaista ty\xf6kokemusta, josta arvioit olevan hy\xf6ty\xe4 hakemassasi teht\xe4v\xe4ss\xe4.', verbose_name='Ty\xf6kokemus')),
                ('shift_wishes', models.TextField(blank=True, help_text='Jos tied\xe4t nyt jo, ettet p\xe4\xe4se paikalle johonkin tiettyyn aikaan tai haluat osallistua johonkin tiettyyn ohjelmanumeroon, mainitse siit\xe4 t\xe4ss\xe4.', verbose_name='Alustavat ty\xf6vuorotoiveet')),
                ('free_text', models.TextField(blank=True, help_text='Jos haluat sanoa hakemuksesi k\xe4sittelij\xf6ille jotain sellaista, jolle ei ole omaa kentt\xe4\xe4 yll\xe4, k\xe4yt\xe4 t\xe4t\xe4 kentt\xe4\xe4.', verbose_name='Vapaa alue')),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='yukicon2017_signup_extras', to='core.Event')),
                ('person', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='yukicon2017_signup_extra', to='core.Person')),
            ],
            options={
                'abstract': False,
            },
            bases=(labour.models.signup_extras.SignupExtraMixin, models.Model),
        ),
        migrations.CreateModel(
            name='SpecialDiet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=63)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='signupextra',
            name='special_diet',
            field=models.ManyToManyField(blank=True, to='yukicon2017.SpecialDiet', verbose_name='Erikoisruokavalio'),
        ),
        migrations.AddField(
            model_name='signupextra',
            name='work_days',
            field=models.ManyToManyField(help_text=b'V\xc3\xa4nk\xc3\xa4rit: Min\xc3\xa4 p\xc3\xa4ivin\xc3\xa4 olet halukas ty\xc3\xb6skentelem\xc3\xa4\xc3\xa4n? Ohjelmanj\xc3\xa4rjest\xc3\xa4j\xc3\xa4t: Tarjoatko ohjelmaasi Pyryconiin, Yukiconiin vai kumpaan tahansa?', to='yukicon2017.EventDay', verbose_name='Tapahtumap\xe4iv\xe4t'),
        ),
    ]