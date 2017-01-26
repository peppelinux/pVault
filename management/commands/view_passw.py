# -*- coding: utf-8 -*-
import argparse
import csv
import os

from django.core.management.base import BaseCommand, CommandError

from pVault.models import *


class Command(BaseCommand):
    help = 'View passwd'

    def add_arguments(self, parser):
        parser.add_argument('-u', default='test')

    def handle(self, *args, **options):
        #~ print args
        #~ print options
        from pVault.models import PasswordVault
        u = options['u']
        print '%s password is:' % u
        print PasswordVault.objects.get(username=u).view()
        #~ self.stdout.write("Importazione completata")

