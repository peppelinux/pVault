# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pVault', '0004_auto_20161015_2133'),
    ]

    operations = [
        migrations.AlterField(
            model_name='passwordvault',
            name='on_servers',
            field=models.ManyToManyField(to='pVault.Server', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='passwordvault',
            name='password',
            field=models.CharField(help_text=b'this will be filled with encrypted password encoded as hexlified string', max_length=1024),
        ),
    ]
