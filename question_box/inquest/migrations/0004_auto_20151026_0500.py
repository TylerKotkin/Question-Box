# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inquest', '0003_auto_20151026_0452'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='tag',
        ),
        migrations.AddField(
            model_name='question',
            name='tag',
            field=models.CharField(default='none', max_length=255),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='Tag',
        ),
    ]
