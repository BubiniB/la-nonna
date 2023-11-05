from django.db import models

# Create your models here.
COURSE_CHOICES = (
    ('Antipasti', 'Antipasti'),
    ('Primi Piatti', 'Primi Piatti'),
    ('Secondi Piatti', 'Secondi Piatti'),
    ('Dolci', 'Dolci'),
    ('Bevande', 'Bevande')
)

class Menu(models.Model):
    name = models.CharField(max_length=50)
    course = models.CharField(max_length=50, choices=COURSE_CHOICES)
    description = models.TextField(max_length=500)
    price = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return self.name
