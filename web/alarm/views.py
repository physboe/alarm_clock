from django.shortcuts import render, get_object_or_404, reverse
from django.http import HttpResponseRedirect
from .models import Alarm
from .core_interface import CoreInterfaceImpl


def index(request):
    alarms = Alarm.objects.all()
    print(alarms)
    context = {'alarms': alarms}
    return render(request, 'index.html', context)


def detail(request, alarm_id):
    alarm = get_object_or_404(Alarm, pk=alarm_id)
    return render(request, 'detail.html', {'alarm': alarm})


def save(request, alarm_id):
    try:
        alarm = Alarm.objects.get(pk=alarm_id)
    except Alarm.DoesNotExist:
        alarm = Alarm()

    alarm.name = request.POST.get('name', alarm.name)
    alarm.time = request.POST.get('time', alarm.time)
    alarm.isOn = 'isOn' in request.POST
    alarm.repeat = 'repeat' in request.POST
    alarm.weekdays = request.POST.get('weekdays', alarm.weekdays)
    alarm.save()
    CoreInterfaceImpl.getInstance().put(alarm)
    return HttpResponseRedirect(reverse('index'))


def delete(request, alarm_id):
    alarm = get_object_or_404(Alarm, pk=alarm_id)
    alarm.delete()
    CoreInterfaceImpl.getInstance().remove(alarm)
    return HttpResponseRedirect(reverse('index'))


def new(request):
    alarm = Alarm()
    alarm.id = 0
    alarm.name = "New Alarm"
    return render(request, 'detail.html', {'alarm': alarm})
