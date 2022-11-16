from django.db import models
from django.urls import reverse

# Create your models here.
class Car(models.Model):
    make = models.CharField(max_length=100)
    model = models.CharField(max_length=200)
    year = models.IntegerField()
    description = models.TextField(max_length=250)

    def __str__(self):
        return f"{self.make} {self.model} ({self.id})"

    def get_absolute_url(self):
        return reverse('detail', kwargs={'car_id': self.id})