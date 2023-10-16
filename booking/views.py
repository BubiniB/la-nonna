from django.shortcuts import render, redirect

from .models import Reservation
from .forms import BookTableForm

# Create your views here.
def book_table(request):
    if request.method == 'POST':
        name = request.POST.get('reservation_name')
        email = request.POST.get('reservation_email')
        phone = request.POST.get('reservation_phone')
        party = request.POST.get('reservation_party')
        date = request.POST.get('reservation_date')
        time = request.POST.get('reservation_time')
        Reservation.objects.create(name=name, email=email, phone=phone, party=party, date=date, time=time)

        return redirect('view_reservations')
    form = BookTableForm
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