from datetime import datetime, timedelta
from time import sleep


class PointInTime:

    def __init__(self, point_in_time: datetime):
        self.point_in_time = point_in_time

    def wait_timedelta(self, wait_time: timedelta) -> "PointInTime":
        time_at_end = self.point_in_time + wait_time
        waiting_time = time_at_end - datetime.now()
        print(waiting_time.total_seconds())
        sleep(waiting_time.total_seconds())
        return time_at_end

    def wait_ticks(self, ticks: int) -> "PointInTime":
        return self.wait_timedelta(timedelta(milliseconds=(600 * ticks)))

    def wait_and_update(self, wait_time: timedelta):
        self.point_in_time = self.wait_timedelta(wait_time)

    def wait_ticks_and_update(self, ticks: int):
        self.point_in_time = self.wait_ticks(ticks)


def begin() -> PointInTime:
    return PointInTime(datetime.now())
