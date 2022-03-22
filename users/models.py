from django.db import models

# Create your models here.

class UserBase(models.Model):
    name = models.CharField("name", max_length=30)
    surname = models.CharField("surname", max_length=40)
    age = models.IntegerField("age")

    def __str__(self):
        return f'{self.name} {self.surname}'
    
    def getInitials(self):
        return f'{self.name[0].lower() + self.surname.lower()}'


class Weather(models.Model):
    city = models.CharField("city", max_length=30)
    country = models.CharField("country", max_length=30)
    weather_celcius = models.IntegerField("weather_celsius", default=0)

    def __str__(self):
        return f'{city} {weather_celcius}'
    