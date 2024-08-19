from pynput.keyboard import Key, KeyCode
from super_bot.point_in_time import begin
from super_bot.super_bot import SuperBot

bot = SuperBot()


def gcd_sequence_builder(
        keys_to_press: list[str | Key | KeyCode]) -> callable[[], None]:

    def simple_sequence():
        point_in_time = begin()

        for key in keys_to_press:
            bot.press_key(key)
            point_in_time.wait_ticks_and_update(3)

    return simple_sequence
