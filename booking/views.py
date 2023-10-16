from django.shortcuts import render, redirect

from .models import Reservation
from .forms import BookTableForm

# Create your views here.
def book_table(request):
    if request.method == 'POST':
        form = BookTableForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('view_reservations')
    form = BookTableForm() 
    context = {
        'form': form
    }
    return render(request, 'booking/book_table.html', context)


def view_reservations(request):
    reservation = Reservation.objects.all()
    context = {
        'reservation': reservation
    }
    return render(request, 'booking/view_reservations.html', context)