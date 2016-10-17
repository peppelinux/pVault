# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pVault', '0008_auto_20161016_1315'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='passwordencoding',
            options={'verbose_name_plural': 'Server Storage Model Delete methods'},
        ),
        migrations.RemoveField(
            model_name='passwordencoding',
            name='name',
        ),
    ]
