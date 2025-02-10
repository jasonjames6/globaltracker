import os
import time
import ctypes
from datetime import datetime, timedelta

class GlobalTracker:
    def __init__(self, sleep_hour=23, wake_hour=7):
        self.sleep_hour = sleep_hour
        self.wake_hour = wake_hour
        self.system = ctypes.windll.kernel32

    def set_sleep_schedule(self):
        while True:
            now = datetime.now()
            sleep_time = now.replace(hour=self.sleep_hour, minute=0, second=0, microsecond=0)
            wake_time = now.replace(hour=self.wake_hour, minute=0, second=0, microsecond=0)

            if now.hour >= self.sleep_hour:
                sleep_time += timedelta(days=1)
            if now.hour < self.wake_hour:
                wake_time -= timedelta(days=1)

            if sleep_time < wake_time:
                sleep_time, wake_time = wake_time, sleep_time

            time_to_sleep = (sleep_time - now).total_seconds()
            time_to_wake = (wake_time - now).total_seconds()

            if 0 <= time_to_sleep <= 3600:
                print("System will sleep soon.")
                time.sleep(time_to_sleep)
                self.sleep_system()
            elif 0 <= time_to_wake <= 3600:
                print("System will wake soon.")
                time.sleep(time_to_wake)
                self.wake_system()

            time.sleep(3600)

    def sleep_system(self):
        print("Putting system to sleep...")
        self.system.SetSuspendState(False, True, False)

    def wake_system(self):
        print("Waking system up...")
        # Waking logic is typically handled by BIOS settings or scheduled tasks in Windows.

if __name__ == "__main__":
    tracker = GlobalTracker(sleep_hour=23, wake_hour=7)
    tracker.set_sleep_schedule()