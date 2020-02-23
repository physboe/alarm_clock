import schedule
import time
import threading


class Runner(object):
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
    runner = Runner()
    runner.run()

if __name__ == "__main__":
    main()
