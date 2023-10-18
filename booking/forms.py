from django import forms
from .models import Reservation


# Form that lets users book a table
class BookTableForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = '__all__'


# Form that is used for viewing reservations and cancel them
class ViewReservationForm(forms.Form):
    email = forms.EmailField(label='Email')