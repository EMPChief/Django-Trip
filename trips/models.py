from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
from django.core.exceptions import ValidationError
import datetime  # import datetime if you want to set a default date

class Trip(models.Model):
    city = models.CharField(max_length=200, blank=True, null=True, default='Not Specified')
    country = models.CharField(max_length=200, blank=True, null=True, default='Not Specified')
    start_date = models.DateField(blank=True, null=True, default=datetime.date.today)
    end_date = models.DateField(blank=True, null=True, default=datetime.date.today)
    owner = models.ForeignKey(User, related_name='trips', on_delete=models.CASCADE)
    
    def clean(self):
        if self.start_date and self.end_date:
            if self.start_date > self.end_date:
                raise ValidationError("End date should be greater than start date.")

    def __str__(self):
        return f'Trip to {self.city}, {self.country}'

class Note(models.Model):
    EXCURSION = (
        ('Excursion', 'Excursion'),
        ('Adventure', 'Adventure'),
        ('Hiking', 'Hiking'),
        ('Trekking', 'Trekking'),
        ('Camping', 'Camping'),
        ('Cultural', 'Cultural'),
        ('Other', 'Other'),
    )
    trip = models.ForeignKey(Trip, related_name='notes', on_delete=models.CASCADE)
    note = models.TextField(max_length=500, blank=True, null=True)
    name = models.CharField(max_length=100, blank=True, null=True, default='General')
    type = models.CharField(max_length=100, choices=EXCURSION, blank=True, null=True, default='Other')
    img = models.ImageField(upload_to='notes/', blank=True, null=True)
    rating = models.IntegerField(
        blank=True, 
        null=True, 
        validators=[
            MaxValueValidator(5),
            MinValueValidator(1)
        ],
        default=3
    )

    def __str__(self):
        return f'Note for {self.trip}: {self.note[:20]}...'
