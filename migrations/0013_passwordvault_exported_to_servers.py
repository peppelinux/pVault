# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pVault', '0012_passwordvaulthistory'),
    ]

    operations = [
        migrations.AddField(
            model_name='passwordvault',
            name='exported_to_servers',
            field=models.BooleanField(default=1),
            preserve_default=False,
        ),
    ]
