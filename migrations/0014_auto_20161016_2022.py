# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pVault', '0013_passwordvault_exported_to_servers'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='serverstoragemodel',
            name='access_type',
        ),
        migrations.RemoveField(
            model_name='serverstoragemodel_add',
            name='storage_model',
        ),
        migrations.RemoveField(
            model_name='serverstoragemodel_delete',
            name='storage_model',
        ),
        migrations.RemoveField(
            model_name='serverstoragemodel_modify',
            name='storage_model',
        ),
        migrations.RemoveField(
            model_name='server',
            name='storage_model',
        ),
        migrations.AddField(
            model_name='server',
            name='worker_queue',
            field=models.CharField(help_text=b'the running worker on the server listens to this queue, if needed', max_length=46, null=True, blank=True),
        ),
        migrations.DeleteModel(
            name='ServerAccessType',
        ),
        migrations.DeleteModel(
            name='ServerStorageModel',
        ),
        migrations.DeleteModel(
            name='ServerStorageModel_Add',
        ),
        migrations.DeleteModel(
            name='ServerStorageModel_Delete',
        ),
        migrations.DeleteModel(
            name='ServerStorageModel_Modify',
        ),
    ]
