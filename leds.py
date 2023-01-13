from machine import Pin
import time

ledR = Pin(17, Pin.OUT)
ledY = Pin(19, Pin.OUT)
ledG = Pin(16, Pin.OUT)
timing = 1000


def miga(led, amount):
    for j in range(0, amount):
        led.on()
        time.sleep_ms(timing//2)
        led.off()
        time.sleep_ms(timing//2)
    return


def przebiegRG(run, direction=1, delay=200):
    leds = [ledR, ledY, ledG][::direction]
    for i in range(run*3):
        leds[i % 3].on()
        time.sleep_ms(delay)
        leds[i % 3].off()
        time.sleep_ms(delay)
    return


def flash_all_leds():
    ledR.on()
    ledY.on()
    ledG.on()
    time.sleep_ms(500)
    ledR.off()
    ledY.off()
    ledG.off()


# przebiegRG(3, -1)

# print("Done :)")

# .local/bin/ampy --port /dev/ttyUSB0 run Documents/studia/PIPR/project_elektronika/ledy.py
# flash_all_leds()