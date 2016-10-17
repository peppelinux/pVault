# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pVault', '0015_auto_20161016_2059'),
    ]

    operations = [
        migrations.AlterField(
            model_name='passwordvaultexports',
            name='encoding',
            field=models.ForeignKey(related_name='enc', to='pVault.PasswordEncoding'),
        ),
    ]
