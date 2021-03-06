# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-28 21:00
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.TextField()),
                ('timestamp', models.DateTimeField(auto_now=True, db_index=True)),
                ('handle', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'message',
                'verbose_name_plural': 'messages',
            },
        ),
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('videoId', models.CharField(max_length=200)),
                ('thumb_default', models.URLField(blank=True, null=True)),
                ('thumb_medium', models.URLField(blank=True, null=True)),
                ('thumb_high', models.URLField(blank=True, null=True)),
                ('title', models.CharField(blank=True, max_length=200, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('published_date', models.DateTimeField(auto_now=True)),
                ('closed_date', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'video',
                'verbose_name_plural': 'videos',
            },
        ),
        migrations.AddField(
            model_name='message',
            name='video',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='messages', to='core.Video'),
        ),
    ]
