from django import forms
from .models import Directory, File

class DirectoryForm(forms.ModelForm):
    class Meta:
        model = Directory
        fields = ['name']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
        }

class FileForm(forms.ModelForm):
    class Meta:
        model = File
        fields = ['name', 'file']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'file': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }