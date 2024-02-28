# SPDX-FileCopyrightText: 2024-present Filip Strajnar
#
# SPDX-License-Identifier: Apache-2.0
from pynput import keyboard, mouse
from pynput.mouse import Button
from pynput.keyboard import Key, KeyCode
from secrets import randbelow
from time import sleep
from extra_random import ExtraRandom


class SuperBot:

    def __init__(self):
        self.keyboard = keyboard.Controller()
        self.mouse = mouse.Controller()

    def left_click(self):
        """Click the left mouse button."""
        self.mouse.click(Button.left)

    def right_click(self):
        """Click the right mouse button."""
        self.mouse.click(Button.right)

    def middle_click(self):
        """Click the middle mouse button."""
        self.mouse.click(Button.middle)

    def move_mouse(self, x: int, y: int):
        self.mouse.position = (x, y)

    def random_move_mouse(self, min_x: int, min_y: int, max_x: int,
                          max_y: int):
        x = self.random_between(min_x, max_x)
        y = self.random_between(min_y, max_y)
        self.move_mouse(x, y)

    def type(self, text: str):
        """Types the text provided."""
        self.keyboard.type(text)

    def press_key_holding(self, key: str | Key | KeyCode,
                          hold_keys: list[str | Key | KeyCode]):
        """Presses the key while holding down the `hold_keys`."""
        for hold_key in hold_keys:
            self.keyboard.press(hold_key)

        self.keyboard.tap(key)

        for hold_key in hold_keys:
            self.keyboard.release(hold_key)

    def press_key(self,
                  key: str | Key | KeyCode,
                  hold_ctrl: bool = False,
                  hold_alt: bool = False,
                  hold_shift: bool = False):
        hold_keys = []

        if hold_ctrl:
            hold_keys.append(Key.ctrl)
        if hold_alt:
            hold_keys.append(Key.alt)
        if hold_shift:
            hold_keys.append(Key.shift)

        self.press_key_holding(key, hold_keys)

    def random_between(self, min: int, max: int) -> int:
        delta = max - min
        random_value = randbelow(delta)
        return min + random_value

    def random_sleep(self,
                     min_milliseconds: int,
                     max_milliseconds: int,
                     extra_randomness: list[ExtraRandom] = []) -> int:
        random_duration = self.random_between(min_milliseconds,
                                              max_milliseconds)

        for extra_random in extra_randomness:
            if randbelow(extra_random.one_in) == 0:
                random_duration += self.random_between(extra_random.min,
                                                       extra_random.max)

        print(f"Sleeping for: {random_duration} milliseconds.")
        sleep(random_duration / 1_000)
        return random_duration

    def super_random_sleep(self, min_milliseconds: int,
                           max_milliseconds: int) -> int:
        return self.random_sleep(min_milliseconds, max_milliseconds, [
            ExtraRandom(100, 200, 10),
            ExtraRandom(150, 250, 100),
            ExtraRandom(300, 400, 1_000),
            ExtraRandom(500, 1_000, 10_000),
            ExtraRandom(1000, 10_000, 100_000),
        ])
