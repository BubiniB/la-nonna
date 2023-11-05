from django.shortcuts import render
from .models import Menu

# Create your views here.

# Only one view because there aren't many items for each course 
def menu(request):
    menu_items = Menu.objects.all()
    return render(request, 'menu/menu.html', {'menu_items': menu_items})