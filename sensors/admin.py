from django.contrib import admin
from .models import Temperature, Humidity, ApiKey, Photoresistor

admin.site.register(ApiKey)
admin.site.register(Temperature)
admin.site.register(Humidity)
admin.site.register(Photoresistor)
# Register your models here.
