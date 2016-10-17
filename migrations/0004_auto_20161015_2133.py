# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pVault', '0003_auto_20161015_2133'),
    ]

    operations = [
        migrations.AlterField(
            model_name='passwordvault',
            name='description',
            field=models.CharField(max_length=135, null=True, blank=True),
        ),
    ]
