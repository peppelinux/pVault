# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pVault', '0009_auto_20161016_1320'),
    ]

    operations = [
        migrations.CreateModel(
            name='PasswordVaultExports',
            fields=[
                ('id_tab', models.AutoField(serialize=False, primary_key=True)),
                ('value', models.CharField(max_length=256, null=True, blank=True)),
                ('is_active', models.BooleanField()),
                ('encoding', models.ForeignKey(to='pVault.EncodingFormat')),
                ('password_vault', models.ForeignKey(to='pVault.PasswordVault')),
            ],
            options={
                'verbose_name_plural': 'Password Vault exports',
            },
        ),
        migrations.AlterModelOptions(
            name='passwordencoding',
            options={'verbose_name_plural': 'Password Encoding'},
        ),
    ]
