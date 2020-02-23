import schedule
import time
import threading
from HueServices import HueServiceImpl
from ServicesUtils import RoutineInterface


class ScheduleServiceImpl(object):

    __instance = None

    @staticmethod
    def getInstance():
        if ScheduleServiceImpl.__instance is None:
            ScheduleServiceImpl()
        return ScheduleServiceImpl.__instance

    def __init__(self):
        if ScheduleServiceImpl.__instance is not None:
            raise Exception("This class is a singleton!")
        else:
            ScheduleServiceImpl.__instance = self

    WEEKDAYS = ("Mo", "Di", "Mi", "Do", "Fr", "Sa", "So")

    def createWeekdayJob(self):
        return schedule.every()

    def createEveryDayJob(self):
        return schedule.every(1).day

    def onWeekDays(self, job, *weekdays):
        for weekday in weekdays:
            if(weekday == "Mo"):
                job = job.monday
            elif(weekday == "Di"):
                job = job.tuesday
            elif(weekday == "Mi"):
                job = job.wednesday
            elif(weekday == "Do"):
                job = job.thursday
            elif(weekday == "Fr"):
                job = job.friday
            elif(weekday == "Sa"):
                job = job.saturday
            elif(weekday == "So"):
                job = job.sunday
        return job

    def setTime(self, job, hour, min):
        return job.at(hour + ":" + min)

    def setRoutine(self, job, func, **args):
        return job.do(func, args).tag(args['jobId'])

    def removeJob(self, jobId):
        pass

    def __runLoop__(self):
        try:
            while True:
                schedule.run_pending()
                print(schedule.jobs)
                time.sleep(1)
                if(self.stopNow):
                    break
        except KeyboardInterrupt:
            print("interrupted")
            self.stop()

    def run(self):
        self.runThread = threading.Thread(target=self.__runLoop__)
        self.stopNow = False
        self.runThread.start()

    def stop(self):
        self.stopNow = True
        self.runThread.join()


class RoutinesHandlerImpl(RoutineInterface):

    def doRoutine(self, args):
        print(args['text'])


def main():
    alarmService = ScheduleServiceImpl.getInstance()
    alarmService.run()

    job1 = alarmService.createWeekdayJob()
    job1 = alarmService.onWeekDays(job1, "Mo")
    job1 = alarmService.setTime(job1, "08", "50")

    job2 = alarmService.createEveryDayJob()
    job2 = alarmService.setTime(job2, "13", "07")

    hueService = HueServiceImpl.getInstance()
#    job1 = alarmService.setRepeatAction(job1, 1, hueService.doRoutine, 10)
    job2 = alarmService.setRoutine(job2, hueService.doRoutine, jobId=1, transitionMins=1)


if __name__ == "__main__":
    main()
