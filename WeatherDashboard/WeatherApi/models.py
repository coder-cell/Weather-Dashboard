from django.db import models

# Create your models here.


class Weather(models.Model):
    location = models.CharField(max_length=200)
    temperature = models.FloatField()

    def __str__(self):
        return self.location
