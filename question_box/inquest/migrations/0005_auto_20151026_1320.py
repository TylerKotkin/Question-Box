# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inquest', '0004_auto_20151026_0500'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='tag',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
