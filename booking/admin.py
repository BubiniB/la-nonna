from django.contrib import admin

# Register your models here.
from .models import Reservation, Pictures


admin.site.register(Reservation)
admin.site.register(Pictures)