from django.contrib import admin

from django.contrib.admin.widgets import FilteredSelectMultiple
from django.forms import ModelForm
from django import forms

from models import *

class PasswordVaultExportsForm(forms.ModelForm):
    class Meta:
        model = PasswordVaultExports
        # django 1.8, prevents "Creating a ModelForm without either the 'fields' attribute or the 'exclude' attribute is prohibited;"
        fields = '__all__'        

class PasswordVaultExportsInLine(admin.TabularInline):
    form  = PasswordVaultExportsForm
    model = PasswordVaultExports
    extra = 0

class PasswordVaultHistoryForm(forms.ModelForm):
    class Meta:
        model = PasswordVaultHistory
        # django 1.8, prevents "Creating a ModelForm without either the 'fields' attribute or the 'exclude' attribute is prohibited;"
        fields = '__all__'        

class PasswordVaultHistoryInLine(admin.TabularInline):
    form  = PasswordVaultHistoryForm
    model = PasswordVaultHistory
    extra = 0
