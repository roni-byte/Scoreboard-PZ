from machine import Pin, SoftI2C
from ssd1306 import SSD1306_I2C
import framebuf
import byte_arrays


"""
How to connect:
VCC - 3V3
GND - GND
SCL - D22 e.g.
SDA - D21 e.g.
"""

oled_width = 128
oled_height = 64

def oled1306_configuration(scl_pin=22, sda_pin=21):
    i2c = SoftI2C(scl=Pin(scl_pin), sda=Pin(sda_pin))
    return SSD1306_I2C(oled_width, oled_height, i2c)

oled = oled1306_configuration()

def oled1306_print_result(oled_passed: "SSD1306_I2C", buffer1, buffer2):
    fb = framebuf.FrameBuffer(buffer1, 32, 64, framebuf.MONO_HLSB)
    fb2 = framebuf.FrameBuffer(buffer2, 32, 64, framebuf.MONO_HLSB)
    fb3 = framebuf.FrameBuffer(byte_arrays.buffer_, 64, 64, framebuf.MONO_HLSB)

    oled_passed.framebuf.blit(fb, 0, 0)
    oled_passed.framebuf.blit(fb2, 96, 0)
    oled_passed.framebuf.blit(fb3, 32, 0)

    oled_passed.invert(1)
    oled_passed.show()

oled1306_print_result(oled, byte_arrays.buffer_0, byte_arrays.buffer_4)
#sprawdz buffer_0

