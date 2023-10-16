from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from datetime import datetime

# Choices for party size
PARTY_SIZE = (
    ("2", "2"),
    ("3", "3"),
    ("4", "4"),
    ("5", "5"),
    ("6", "6")
)

# Choices for time slots
TIME_SLOTS = (
    ("18:00", "18:00"),
    ("18:15", "18:15"),
    ("18:30", "18:30"),
    ("18:45", "18:45"),
    ("19:00", "19:00"),
    ("19:15", "19:15"),
    ("19:30", "19:30"),
    ("19:45", "19:45"),
    ("20:00", "20:00"),
    ("20:15", "20:15"),
    ("20:30", "20:30"),
    ("20:45", "20:45")    
)


# Reservation Details
class Reservation(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False)
    email = models.EmailField(db_index=True, unique=True, null=False, blank=False)
    phone = PhoneNumberField(null=False, blank=False)
    party = models.CharField(max_length=50, choices=PARTY_SIZE, default="2")
    date = models.DateField(default=datetime.now)
    time = models.CharField(max_length=10, choices=TIME_SLOTS, blank=False)


    def __str__(self):
        return self.name
