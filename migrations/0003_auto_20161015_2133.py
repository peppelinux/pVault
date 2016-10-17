# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pVault', '0002_encodingformat_example'),
    ]

    operations = [
        migrations.AlterField(
            model_name='encodingformat',
            name='example',
            field=models.CharField(help_text=b"codes a 'hello!' string", max_length=128, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='passwordvault',
            name='password',
            field=models.CharField(help_text=b'this will be filled with encrypted password encoded as base64 string', max_length=1024),
        ),
    ]
