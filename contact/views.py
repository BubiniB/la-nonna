from django.shortcuts import render

from .models import Contact

# Create your views here.
def contact_us(request):
    if request.method == 'POST':

