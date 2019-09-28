from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('temperature/', views.temperature),
    path('photoresistor/', views.photoresistor),
]