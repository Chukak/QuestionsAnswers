# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-01-26 19:57
from __future__ import unicode_literals

import apps.accounts.models
import apps.accounts.validators
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_auto_20180123_1802'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='avatar',
            field=models.ImageField(blank=True, db_column='avatar', error_messages={'invalid': 'Please choice a valid image format.'}, upload_to=apps.accounts.models.upload_avatar_path, validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['png', 'bw', 'im', 'jp2', 'flc', 'emf', 'ps', 'hdf', 'bufr', 'jpg', 'cur', 'mpg', 'tif', 'jpx', 'xpm', 'pcd', 'webp', 'fits', 'mpo', 'pgm', 'eps', 'ftc', 'msp', 'wmf', 'tiff', 'ftu', 'pdf', 'jpeg', 'j2c', 'rgb', 'palm', 'mpeg', 'icns', 'gif', 'j2k', 'jpc', 'grib', 'iim', 'pxr', 'fit', 'pcx', 'psd', 'dcx', 'ppm', 'ras', 'jfif', 'pbm', 'gbr', 'xbm', 'h5', 'jpf', 'sgi', 'tga', 'jpe', 'fli', 'rgba', 'dds', 'ico', 'bmp'])], verbose_name='avatar'),
        ),
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(db_column='username', error_messages={'invalid': 'Enter a valid username.', 'unique': 'A user with this name already exists.'}, help_text='Required. 32 character or fewer. Letters, digits and ./-/_ only.', max_length=32, unique=True, validators=[apps.accounts.validators.validate_username], verbose_name='username'),
        ),
    ]