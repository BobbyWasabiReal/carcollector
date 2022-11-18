from django.db import models
from django.urls import reverse

USES = (
    ('P', 'Performance'),
    ('A', 'Aesthetic'),
    ('S', 'Saftey'),
    ('PA', 'Performance & Aesthetic'),
    ('PS', 'Performance & Saftey'),
    ('SA', 'Saftey & Aesthetic'),
    ('A', 'All'),
)

class Track(models.Model):
    track = models.CharField(max_length=200)
    location = models.CharField(
        max_length=500,
        default='USA'
        )

    def __str__(self):
        return self.track

    def get_absolute_url(self):
        return reverse('tracks_detail', kwargs={'pk': self.id})

class Car(models.Model):
    make = models.CharField(max_length=100)
    model = models.CharField(max_length=200)
    year = models.IntegerField()
    description = models.TextField(max_length=250)
    tracks = models.ManyToManyField(Track)

    def __str__(self):
        return f"{self.make} {self.model} ({self.id})"

    def get_absolute_url(self):
        return reverse('detail', kwargs={'car_id': self.id})

class Mod(models.Model):
    part = models.CharField(max_length=300)
    use = models.CharField(
        max_length=2,
        choices=USES,
        default=USES[0][0]
    )

    car = models.ForeignKey(Car, on_delete=models.CASCADE)

    def __str__(self):
        return f"The {self.part} is/are a {self.get_use_display()} mod"