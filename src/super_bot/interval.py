from datetime import timedelta, datetime
from typing import Callable


class Interval:

    def __init__(self, repeat_interval: timedelta, action: Callable[[], None]):
        self.repeat_interval = repeat_interval
        self.action = action
        self.last_used = datetime.now() - repeat_interval

    def check_and_execute(self):
        if (self.last_used + self.repeat_interval) < datetime.now():
            self.action()
            self.last_used = datetime.now()
