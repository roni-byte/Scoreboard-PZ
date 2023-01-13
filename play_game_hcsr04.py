from machine import Pin, SoftI2C, ADC
from hcsr04 import HCSR04
import SSD1306_OLED
import time


i2c = SoftI2C(scl=Pin(22), sda=Pin(21))

oled_width = 128
oled_height = 64
oled = SSD1306_OLED.SSD1306_I2C(oled_width, oled_height, i2c)
import time

sensor_right = HCSR04(trigger_pin=5, echo_pin=18, echo_timeout_us=10000)
sensor_left = HCSR04(trigger_pin=13, echo_pin=14, echo_timeout_us=10000)



def who_scored():
    while True:
        distance_right = sensor_right.distance_cm()
        distance_left = sensor_left.distance_cm()
        if (distance_right < 5 and distance_right > 0):
            # print('right')
            return 'right'
        if (distance_left < 5 and distance_left > 0):
             return 'left'

        # print('Distance:', distance_right, 'cm')
        # print('Distance:', distance_left, 'cm')

        time.sleep_ms(200)

# print(who_scored())
