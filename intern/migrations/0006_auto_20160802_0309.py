# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-08-02 01:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('intern', '0005_internrole_access_given'),
    ]

    operations = [
        migrations.AlterField(
            model_name='internrole',
            name='comments',
            field=models.CharField(blank=True, max_length=1300, null=True),
        ),
    ]
