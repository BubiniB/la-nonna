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
            # Get the date and the time from the form
            date = form.cleaned_data['date']
            time = form.cleaned_data['time']

            # Check if there is an existing reservation for the same date and time
            existing_reservation = Reservation.objects.filter(date=date, time=time).first()

            if existing_reservation:
                return render(request, 'booking/booking_full.html')
            
            newest_reservation = form.save()
            return redirect('reservation_success', pk=newest_reservation.pk)
            
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


def reservation_success(request, pk):
    newest_reservation = Reservation.objects.latest('pk')
    print(newest_reservation)
    return render(request, 'booking/reservation_success.html', {'newest_reservation': newest_reservation})
