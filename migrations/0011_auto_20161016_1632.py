# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pVault', '0010_auto_20161016_1620'),
    ]

    operations = [
        migrations.RenameField(
            model_name='passwordvault',
            old_name='exported_on_servers',
            new_name='export_to_servers',
        ),
    ]
