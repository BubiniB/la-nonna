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
            messages.success(request, 'Thank you for reaching out! We have successfully received your message and will contact you as soon as possible.')
            return redirect('contact_us')

    context = {
        'form': form
    }

    return render(request, 'contact/contact_us.html', context)

