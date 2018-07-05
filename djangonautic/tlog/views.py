from django.http import HttpResponse
from django.shortcuts import render
from . models import Logger

# Create your views here.
def log_list(request):
    logs = Logger.objects.all().order_by('date');
    return render(request, 'tlog/log_list.html', {'logs':logs})

def log_d(request, slug):
    # return HttpResponse(slug)
    dLogs = Logger.objects.all().filter(slug=slug).order_by('date');
    return render(request, 'tlog/log_list.html', {'logs':dLogs})
