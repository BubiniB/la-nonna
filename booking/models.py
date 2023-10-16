from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

# Customers
class Customer(models.Model):
    first_name = models.CharField(max_length=50, null=False, blank=False)
    last_name = models.CharField(max_length=50, null=False, blank=False)
    email = models.EmailField(db_index=True, unique=True, null=False, blank=False)
    phone = PhoneNumberField(null=False, blank=False)