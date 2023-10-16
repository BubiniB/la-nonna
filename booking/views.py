from django.shortcuts import render

from .models import Reservation
from .forms import BookTableForm

# Create your views here.
def book_table(request):
    return render(request, 'booking/book_table.html', context)


def view_reservations(request):
    reservation = Reservation.objects.all()
    context = {
        'reservation': reservation
    }
    return render(request, 'booking/view_reservations.html', context)