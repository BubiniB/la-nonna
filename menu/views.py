from django.shortcuts import render
from .models import Menu

# Create your views here.

# One view for each course for scalability
def menu_antipasti(request):
    menu_antipasti = Menu.objects.filter(course = 'Antipasti')
    return render(request, 'menu.html', {'menu_antipasti': menu_antipasti})


def menu_primi(request):
    menu_primi = Menu.objects.filter(course = 'Primi Piatti')
    return render(request, 'menu.html', {'menu_primi': menu_primi})


def menu_secondi(request):
    menu_secondi = Menu.objects.filter(course = 'Secondi Piatti')
    return render(request, 'menu.html', {'menu_secondi': menu_secondi})


def menu_dolci(request):
    menu_dolci = Menu.objects.filter(course = 'Dolci')
    return render(request, 'menu.html', {'menu_dolci': menu_dolci})


def menu_bevande(request):
    menu_bevande = Menu.objects.filter(course = 'Bevande')
    return render(request, 'menu.html', {'menu_bevande': menu_bevande})