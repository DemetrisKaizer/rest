from django.shortcuts import render
from .models import Temperature, ApiKey, Photoresistor
from .date_time import get_time
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse



def index(request):
    return render(request, 'index.html')


@csrf_exempt
def temperature(request):
    if request.POST:
        if ApiKey.objects.filter(api_key=request.POST['api_key']):
            obj = Temperature()
            obj.temperature = request.POST['current_temperature']
            obj.time = get_time()
            obj.save()
        else:
            return HttpResponse("Sorry wrong api key.")
        return HttpResponse("It worked!")
    return render(request, 'index.html')


@csrf_exempt
def photoresistor(request):
    if request.POST:
        if ApiKey.objects.filter(api_key=request.POST['api_key']):
            obj = Photoresistor()
            obj.photo_resistance = request.POST['current_photo_resistance']
            obj.time = get_time()
            obj.save()
        else:
            return HttpResponse("Sorry wrong api key.")
        return HttpResponse("It worked!")
    return render(request, 'index.html')