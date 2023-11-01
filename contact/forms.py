from django import forms
from .models import Contact


# Form that lets users book a table
class BookTableForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'

        widget = {
            'name': form.TextInput(attrs={"class": "form-control"}),
            'email': form.EmailInput(attrs={"class": "form-control"}),
            'subject': form.Textarea(attrs={"class": "form-control"}),
        }