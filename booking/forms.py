from django import forms
from .models import Reservation


# Form that lets users book a table
class BookTableForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = '__all__'

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'phone': forms.NumberInput(attrs={'class': 'form-control'}),

            'number_of_persons': forms.Select(attrs={'class': 'form-control'}),
            'date': forms.DateInput(attrs={'type': 'date', 'placeholder': 'yyyy-mm-dd (DOB)', 'class': 'form-control'}),
            'time': forms.Select(attrs={'class': 'form-control'}),
        }


# Form that is used for viewing reservations and cancel them
class ViewReservationForm(forms.Form):
    email = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={'class': 'form-control'}))
