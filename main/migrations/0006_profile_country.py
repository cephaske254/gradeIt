# Generated by Django 3.0.7 on 2020-06-07 16:29

from django.db import migrations
import django_countries.fields


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_savedarticle'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='country',
            field=django_countries.fields.CountryField(default='', max_length=2),
            preserve_default=False,
        ),
    ]
