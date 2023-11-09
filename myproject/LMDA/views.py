from django.shortcuts import render
from .models import Locomotive, Brigade, Repair, Worker

def index(request):
    locomotives = Locomotive.objects.all()
    brigades = Brigade.objects.all()
    repairs = Repair.objects.all()
    workers = Worker.objects.all()
    context = {
        'locomotives': locomotives,
        'brigades': brigades,
        'repairs': repairs,
        'workers': workers,
    }
    return render(request, 'LMDA/index.html', context)


