from machine import Pin, I2C
import sh1106

i2c = I2C(scl=Pin(22), sda=Pin(21), freq=200000)
display = sh1106.SH1106_I2C(128, 64, i2c, None, 0x3c)
display.sleep(False)
display.fill(0)
display.rect(0, 0, 128, 32, 1)
display.show()
