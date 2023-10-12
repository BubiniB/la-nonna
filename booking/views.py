from django.shortcuts import render

# Create your views here.
def book_table(request):
    return render(request, 'booking/book_table.html') 