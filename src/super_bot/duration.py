# SPDX-FileCopyrightText: 2024-present Filip Strajnar
#
# SPDX-License-Identifier: Apache-2.0
from datetime import timedelta, datetime


class Duration():

    def __init__(self, duration: timedelta):
        self.start = datetime.now()
        self.end = self.start + duration

    def keep_running(self) -> bool:
        return self.end > datetime.now()


def run_for_minutes(minutes: int) -> Duration:
    return Duration(timedelta(minutes=minutes))


def run_for_hours(hours: int) -> Duration:
    return Duration(timedelta(hours=hours))
