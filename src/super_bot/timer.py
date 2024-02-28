# SPDX-FileCopyrightText: 2024-present Filip Strajnar
#
# SPDX-License-Identifier: Apache-2.0
from datetime import timedelta, datetime


class Timer():

    def __init__(self, duration: timedelta):
        self.start = datetime.now()
        self.end = self.start + duration

    def expired(self) -> bool:
        return self.end < datetime.now()

    def ongoing(self) -> bool:
        return self.end > datetime.now()


def minutes(minutes: int) -> Timer:
    return Timer(timedelta(minutes=minutes))


def hours(hours: int) -> Timer:
    return Timer(timedelta(hours=hours))
