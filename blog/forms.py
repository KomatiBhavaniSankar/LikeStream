from django import forms
from django.contrib.auth.models import User
from .models import comment


class CommentForm(forms.ModelForm):
    class Meta:
        model = comment
        fields = ('name', 'body')

        widgets = {
            'Name': forms.TextInput(attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
        }

