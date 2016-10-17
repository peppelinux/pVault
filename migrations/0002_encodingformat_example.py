# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pVault', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='encodingformat',
            name='example',
            field=models.CharField(default='sdasdasd', max_length=128),
            preserve_default=False,
        ),
    ]
