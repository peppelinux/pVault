# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EncodingFormat',
            fields=[
                ('id_tab', models.AutoField(serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=12)),
                ('function', models.CharField(max_length=33, choices=[(b'md5', b'pVault_MD5'), (b'salted_md5', b'pVault_Salted_MD5'), (b'ntlm', b'pVault_NTLM')])),
            ],
            options={
                'ordering': ['name'],
                'verbose_name_plural': 'Encoding formats',
            },
        ),
        migrations.CreateModel(
            name='PasswordEncoding',
            fields=[
                ('id_tab', models.AutoField(serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=33)),
                ('date_creation', models.DateTimeField(auto_now=True)),
                ('iv', models.CharField(max_length=256, null=True, blank=True)),
                ('secret', models.CharField(max_length=256, null=True, blank=True)),
                ('salt', models.CharField(max_length=256, null=True, blank=True)),
                ('is_active', models.BooleanField()),
                ('encoding', models.ForeignKey(to='pVault.EncodingFormat')),
            ],
            options={
                'ordering': ['storage_model __name'],
                'verbose_name_plural': 'Server Storage Model Delete methods',
            },
        ),
        migrations.CreateModel(
            name='PasswordVault',
            fields=[
                ('id_tab', models.AutoField(serialize=False, primary_key=True)),
                ('date_creation', models.DateTimeField(auto_now=True)),
                ('username', models.CharField(max_length=135)),
                ('password', models.TextField(help_text=b'this will be filled with encrypted password encoded as base64 string', max_length=1024)),
                ('description', models.CharField(max_length=135)),
                ('is_active', models.BooleanField()),
            ],
            options={
                'ordering': ['username'],
                'verbose_name_plural': 'Password Vault (users credentials)',
            },
        ),
        migrations.CreateModel(
            name='Server',
            fields=[
                ('id_tab', models.AutoField(serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=135)),
                ('date_creation', models.DateTimeField(auto_now=True)),
                ('description', models.TextField(max_length=512, null=True, blank=True)),
                ('is_active', models.BooleanField()),
                ('ip', models.CharField(max_length=46)),
                ('password_encoding', models.ForeignKey(to='pVault.PasswordEncoding')),
            ],
            options={
                'ordering': ['name'],
                'verbose_name_plural': 'Servers',
            },
        ),
        migrations.CreateModel(
            name='ServerAccessType',
            fields=[
                ('id_tab', models.AutoField(serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=12, verbose_name=b'Protocol name')),
                ('date_creation', models.DateTimeField(auto_now=True)),
                ('description', models.TextField(max_length=512, null=True, blank=True)),
                ('port_number', models.IntegerField()),
            ],
            options={
                'ordering': ['name'],
                'verbose_name_plural': 'Server Access Types',
            },
        ),
        migrations.CreateModel(
            name='ServerStorageModel',
            fields=[
                ('id_tab', models.AutoField(serialize=False, primary_key=True)),
                ('date_creation', models.DateTimeField(auto_now=True)),
                ('description', models.TextField(max_length=512)),
                ('append', models.BooleanField(help_text=b'If a new object should be appendend or the entire definition must be regenerated.')),
                ('is_active', models.BooleanField()),
                ('access_type', models.ForeignKey(to='pVault.ServerAccessType')),
            ],
            options={
                'ordering': ['server__name'],
                'verbose_name_plural': 'Server Storage Models',
            },
        ),
        migrations.CreateModel(
            name='ServerStorageModel_Add',
            fields=[
                ('id_tab', models.AutoField(serialize=False, primary_key=True)),
                ('date_creation', models.DateTimeField(auto_now=True)),
                ('template', models.TextField(max_length=1024)),
                ('is_active', models.BooleanField()),
                ('storage_model', models.ForeignKey(to='pVault.ServerStorageModel')),
            ],
            options={
                'ordering': ['storage_model __name'],
                'verbose_name_plural': 'Server Storage Model Add methods',
            },
        ),
        migrations.CreateModel(
            name='ServerStorageModel_Delete',
            fields=[
                ('id_tab', models.AutoField(serialize=False, primary_key=True)),
                ('date_creation', models.DateTimeField(auto_now=True)),
                ('template', models.TextField(max_length=1024)),
                ('is_active', models.BooleanField()),
                ('storage_model', models.ForeignKey(to='pVault.ServerStorageModel')),
            ],
            options={
                'ordering': ['storage_model __name'],
                'verbose_name_plural': 'Server Storage Model Delete methods',
            },
        ),
        migrations.CreateModel(
            name='ServerStorageModel_Modify',
            fields=[
                ('id_tab', models.AutoField(serialize=False, primary_key=True)),
                ('date_creation', models.DateTimeField(auto_now=True)),
                ('template', models.TextField(max_length=1024)),
                ('is_active', models.BooleanField()),
                ('storage_model', models.ForeignKey(to='pVault.ServerStorageModel')),
            ],
            options={
                'ordering': ['storage_model __name'],
                'verbose_name_plural': 'Server Storage Model Modify methods',
            },
        ),
        migrations.AddField(
            model_name='server',
            name='storage_model',
            field=models.ForeignKey(to='pVault.ServerStorageModel'),
        ),
        migrations.AddField(
            model_name='passwordvault',
            name='on_servers',
            field=models.ManyToManyField(to='pVault.ServerStorageModel', null=True, blank=True),
        ),
    ]
