from django.shortcuts import render

from .models import Contact
from .forms import ContactForm

# Create your views here.
def contact_us(request):
    form = ContactForm()

    if request.method == 'POST':
        form = ContactForm(request.POST)

        if form.is_valid():
            form.save()

    context = {
        'form': form
    }

    return render(request, 'contact/contact_us.html', context)

