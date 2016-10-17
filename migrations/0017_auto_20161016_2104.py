# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pVault', '0016_auto_20161016_2101'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='passwordvaultexports',
            name='encoding',
        ),
        migrations.AddField(
            model_name='passwordvaultexports',
            name='password_encoding',
            field=models.ForeignKey(default=1, to='pVault.PasswordEncoding'),
            preserve_default=False,
        ),
    ]
