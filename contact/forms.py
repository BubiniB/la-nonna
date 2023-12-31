from django import forms
from .models import Contact


# Form that lets users book a table
class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'subject': forms.Textarea(attrs={'class': 'form-control'}),
        }
        