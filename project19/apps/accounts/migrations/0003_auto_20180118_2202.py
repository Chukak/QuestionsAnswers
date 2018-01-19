# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-01-18 19:02
from __future__ import unicode_literals

import apps.accounts.models
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20180118_2155'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='is_admin',
            field=models.BooleanField(default=False, verbose_name='admin'),
        ),
        migrations.AlterField(
            model_name='user',
            name='avatar',
            field=models.ImageField(blank=True, db_column='avatar', error_messages={'invalid': 'Please choice a valid image format.'}, upload_to=apps.accounts.models.upload_avatar_path, validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['jpf', 'tif', 'jp2', 'pgm', 'ppm', 'msp', 'pxr', 'fits', 'dcx', 'ftc', 'pcx', 'ps', 'png', 'eps', 'mpg', 'jpc', 'jpeg', 'ftu', 'palm', 'xbm', 'icns', 'rgba', 'jfif', 'gif', 'mpeg', 'wmf', 'jpe', 'psd', 'tiff', 'mpo', 'grib', 'bufr', 'im', 'pbm', 'gbr', 'ras', 'h5', 'j2k', 'jpg', 'cur', 'dds', 'tga', 'emf', 'iim', 'bw', 'fit', 'webp', 'ico', 'fli', 'flc', 'xpm', 'pcd', 'sgi', 'hdf', 'bmp', 'rgb', 'j2c', 'jpx', 'pdf'])], verbose_name='avatar'),
        ),
    ]