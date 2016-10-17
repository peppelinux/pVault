# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pVault', '0014_auto_20161016_2022'),
    ]

    operations = [
        migrations.AlterField(
            model_name='passwordvaultexports',
            name='encoding',
            field=models.ForeignKey(to='pVault.PasswordEncoding'),
        ),
        migrations.AlterField(
            model_name='server',
            name='ip',
            field=models.CharField(max_length=46, verbose_name=b'hostname'),
        ),
    ]
