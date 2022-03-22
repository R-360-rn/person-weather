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

class UserLocale(models.Model):
    userbase = models.ForeignKey("app.UserBase", on_delete=models.CASCADE)
    country = models.CharField("country", max_length=20)
    city = models.CharField("city", max_length=20)
    state = models.CharField("state", max_length=20)
    postcode = models.CharField("postcode", max_length=20)
    street = models.CharField("street", max_length=50)

    def __str__(self):
        return f'{userbase} {street}'

class UserContactData(models.Model):
    userbase = models.ForeignKey("app.UserBase", on_delete=models.CASCADE)
    email = models.CharField("email", max_length=50)
    cell = models.CharField("", max_length=20)
    picture = models.BinaryField("picture")

    def __str__(self):
        return f'{email} {cell}'

class Weather(models.Model):
    userbase = models.ForeignKey("app.UserBase", on_delete=models.CASCADE)
    city = models.CharField("city", max_length=30)
    country = models.CharField("country", max_length=30)
    celcius = models.IntegerField("celsius", default=0)
    fahrenheit = models.IntegerField("fahrenheit", default=0)
    wind = models.IntegerField("wind m/s", default=0)

    def __str__(self):
        return f'{city} {weather_celcius}'
    