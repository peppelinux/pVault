# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pVault', '0011_auto_20161016_1632'),
    ]

    operations = [
        migrations.CreateModel(
            name='PasswordVaultHistory',
            fields=[
                ('id_tab', models.AutoField(serialize=False, primary_key=True)),
                ('date', models.DateTimeField(auto_now=True)),
                ('value', models.CharField(max_length=256, null=True, blank=True)),
                ('password_vault', models.ForeignKey(to='pVault.PasswordVault')),
            ],
            options={
                'verbose_name_plural': 'Password Vault history',
            },
        ),
    ]
