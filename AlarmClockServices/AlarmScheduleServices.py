import schedule
import time
import threading
from HueServices import HueServiceImpl

class AlarmScheduleServiceImpl:
    WEEKDAYS = ("Mo","Di","Mi","Do","Fr","Sa","So")

    def createJob(self):
        return schedule.every()

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

    def setAction(self, job, jobId, func, mins):
        return job.do(func, mins).tag(jobId)

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



def main():
    alarmService = AlarmScheduleServiceImpl()
    alarmService.run()

    job1 = alarmService.createJob()
    job1 = alarmService.onWeekDays(job1, "So")
    job1 = alarmService.setTime(job1, "08", "50")

    hueService = HueServiceImpl()
    job1 = alarmService.setAction(job1, 1, hueService.doRoutine, 10)

if __name__ == "__main__":
    main()
