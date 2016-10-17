# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pVault', '0007_passwordvault_exported_on_servers'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='passwordencoding',
            options={'ordering': ['name'], 'verbose_name_plural': 'Server Storage Model Delete methods'},
        ),
        migrations.AlterModelOptions(
            name='serverstoragemodel',
            options={'verbose_name_plural': 'Server Storage Models'},
        ),
        migrations.AlterModelOptions(
            name='serverstoragemodel_add',
            options={'verbose_name_plural': 'Server Storage Model Add methods'},
        ),
        migrations.AlterModelOptions(
            name='serverstoragemodel_delete',
            options={'verbose_name_plural': 'Server Storage Model Delete methods'},
        ),
        migrations.AlterModelOptions(
            name='serverstoragemodel_modify',
            options={'verbose_name_plural': 'Server Storage Model Modify methods'},
        ),
        migrations.RemoveField(
            model_name='serverstoragemodel',
            name='description',
        ),
        migrations.AddField(
            model_name='serverstoragemodel',
            name='name',
            field=models.CharField(default='mysql+sshtunnel', max_length=512),
            preserve_default=False,
        ),
    ]
