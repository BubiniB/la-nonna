from django.shortcuts import render, redirect

from .models import Reservation
from .forms import BookTableForm, ViewReservationForm


# Create your views here.
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
    if reservation:
        if request.method == 'POST' and 'cancel_reservation' in request.POST:
            reservation.delete()
            return redirect('view_reservations')

    return render(request, 'booking/view_reservations.html', context)