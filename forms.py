from django import forms
from .models import PasswordVault

class PasswordVaultForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = PasswordVault
        fields = '__all__'
