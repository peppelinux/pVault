# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pVault', '0006_remove_passwordvault_on_servers'),
    ]

    operations = [
        migrations.AddField(
            model_name='passwordvault',
            name='exported_on_servers',
            field=models.ManyToManyField(to='pVault.Server', null=True, blank=True),
        ),
    ]
