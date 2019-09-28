from django.contrib import admin
from .models import Temperature, Humidity, ApiKey, Photoresistor, Test

admin.site.register(ApiKey)
admin.site.register(Temperature)
admin.site.register(Humidity)
admin.site.register(Photoresistor)
admin.site.register(Test)
# Register your models here.
