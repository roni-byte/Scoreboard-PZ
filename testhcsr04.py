# ----------------------
print("eoo")
from hcsr04 import HCSR04
import time
sensor = HCSR04(trigger_pin=4, echo_pin=19, echo_timeout_us=10000)
run = True
while run:
    distance =sensor.distance_cm()
    if distance == 250.0:
        print("blad pomiaru")
    if distance < 5:
        print("gol")
        time.sleep(1)
    print(distance)

