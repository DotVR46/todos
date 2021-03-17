from django import forms
from .models import Contact


class ContactAddForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'tel_number', 'email']
        widgets = {
            'name': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 1
            }),
            'tel_number': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 1
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control'
            })
        }