from django import forms
from .models import ToDo


class ToDoForm(forms.ModelForm):
    class Meta:
        model = ToDo
        fields = ['title', 'description', 'category']
        widgets = {
            'title': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 1,
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-control',
            }),
            'category': forms.Select(attrs={
                'class': 'form-control'
            })
        }