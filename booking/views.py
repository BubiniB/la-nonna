from django.shortcuts import render, redirect
from datetime import datetime

from .models import Reservation
from .forms import BookTableForm, ViewReservationForm


# Table reservation
def book_table(request):
    form = BookTableForm()

    if request.method == 'POST':
        form = BookTableForm(request.POST)

        if form.is_valid():
            form.save()

        return redirect('view_reservations')
            
    
    context = {
        'form': form
    }
    return render(request, 'booking/book_table.html', context)


# Viewing table reservation
def view_reservations(request):
    reservation = None

    if request.method == 'POST':
        view_form = ViewReservationForm(request.POST)

        if view_form.is_valid():
            email = view_form.cleaned_data['email']
            reservation = Reservation.objects.filter(email=email).first()
    else:
        view_form = ViewReservationForm(request.POST)

    context = {
        'view_form': view_form,
        'reservation': reservation,
    }

    return render(request, 'booking/view_reservations.html', context)
