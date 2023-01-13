from machine import Pin, SoftI2C, ADC
from hcsr04 import HCSR04
import SSD1306_OLED
import time

DELAY = 5  # number of seconds between goals
push_button_left = Pin(13, Pin.IN)
push_button_right = Pin(14, Pin.IN)

i2c = SoftI2C(scl=Pin(22), sda=Pin(21))

oled_width = 128
oled_height = 64
oled = SSD1306_OLED.SSD1306_I2C(oled_width, oled_height, i2c)
import time

sensor_right = HCSR04(trigger_pin=5, echo_pin=18, echo_timeout_us=10000)
sensor_left = HCSR04(trigger_pin=13, echo_pin=14, echo_timeout_us=10000)


def who_scored(left=1, right=1):
    # left and right and by default equal to 1, because it's only matters if this is first goal
    # left, right - score of left player, score of right player
    # maybe we shouldn't delay first goal
    start = time.time()
    while True:
        distance_right = sensor_right.distance_cm()
        distance_left = sensor_left.distance_cm()

        try:
            logic_state_left_button = push_button_left.value()
            if logic_state_left_button is True:
                return "left_button"

            logic_state_right_button = push_button_right.value()
            if logic_state_right_button is True:
                return "right_button"
        except:
            pass

        if (distance_right < 5 and distance_right > 0):
            if left == 0 and right == 0:
                return 'right'
            end = time.time()
            elapsed_time = end - start
            if elapsed_time > DELAY:
                return 'right'
            else:
                print(
                    "Goal detected, but not enough time between last goal and currect one")
        # if (distance_left < 5):
        #      return 'left'

        # print('Distance:', distance_right, 'cm')
        # print('Distance:', distance_left, 'cm')

        time.sleep_ms(200)

# print(who_scored())
