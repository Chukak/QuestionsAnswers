# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-01-22 17:52
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('answers', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='question_id',
            field=models.ForeignKey(db_column='question_id', on_delete=django.db.models.deletion.CASCADE, to='questions.Question', verbose_name='question id'),
        ),
    ]
