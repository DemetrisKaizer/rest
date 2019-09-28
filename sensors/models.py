from django.db import models


class ApiKey(models.Model):
    api_key = models.CharField(max_length=50)

class Test(models.Model):
    api_key = models.CharField(max_length=50)

class Temperature(models.Model):
    temperature = models.DecimalField(decimal_places=2, max_digits=5)
    time = models.DateTimeField(default=0)

    def __str__(self):
        return str(self.temperature) + " (" + self.time.strftime("%Y-%m-%d %H:%M") + ")"


class Humidity(models.Model):
    humidity = models.IntegerField()
    time = models.DateTimeField()

    def __str__(self):
        return str(self.humidity) + " (" + self.time.strftime("%Y-%m-%d %H:%M") + ")"


class Photoresistor(models.Model):
    photo_resistance = models.IntegerField()
    time = models.DateTimeField()

    def __str__(self):
        return str(self.photo_resistance) + " (" + self.time.strftime("%Y-%m-%d %H:%M") + ")"
