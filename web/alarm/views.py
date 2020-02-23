from django.shortcuts import render, get_object_or_404, reverse
from django.http import HttpResponse, HttpResponseRedirect
from .models import Alarm


def index(request):
    alarms = Alarm.objects.all()
    print(alarms)
    context = {'alarms': alarms}
    return render(request, 'index.html', context)


def detail(request, alarm_id):
    alarm = get_object_or_404(Alarm, pk=alarm_id)
    return render(request, 'detail.html', {'alarm': alarm})


def save(request, alarm_id):
    alarm = get_object_or_404(Alarm, pk=alarm_id)
    alarm.name = request.POST.get('name', alarm.name)
    alarm.time = request.POST.get('time', alarm.name)
    alarm.save()
    return HttpResponseRedirect(reverse('index'))


def new(request):
    return HttpResponse("new")


def savenew(request):
    return HttpResponse("savenew")
