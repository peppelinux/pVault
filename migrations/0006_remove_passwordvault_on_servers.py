# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pVault', '0005_auto_20161016_1250'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='passwordvault',
            name='on_servers',
        ),
    ]
