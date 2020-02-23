from alarm_core.schedule_services import ScheduleServiceImpl
from alarm_core.hue_services import HueServiceImpl


class CoreInterfaceImpl(object):
    __instance = None

    @staticmethod
    def getInstance():
        if CoreInterfaceImpl.__instance is None:
            CoreInterfaceImpl()
        return CoreInterfaceImpl.__instance

    def __init__(self):
        if CoreInterfaceImpl.__instance is not None:
            raise Exception("This class is a singleton!")
        else:
            CoreInterfaceImpl.__instance = self

    def put(self, alarm):

        sched = ScheduleServiceImpl.getInstance()
        sched.removeJob(alarm.id)
        if(alarm.isOn):
            if(alarm.repeat):
                job = sched.createWeekdayJob()
                job = sched.onWeekDays(job, alarm.weekdays.split(','))
            else:
                job = sched.createEveryDayJob()

            job = sched.setTime(job, alarm.time)
            hueService = HueServiceImpl.getInstance()
            job = sched.setRoutine(job, hueService.doRoutine, jobId=alarm.id, transitionMins=1)
