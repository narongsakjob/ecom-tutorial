# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-09-07 11:58
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('profiles', '0002_profile_description'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserStripe',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stripe_id', models.CharField(blank=True, max_length=200, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='profile',
            name='user',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='profile',
            name='description',
            field=models.TextField(default='Description'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='name',
            field=models.CharField(max_length=120),
        ),
    ]
