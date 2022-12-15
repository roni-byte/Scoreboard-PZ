# ----------------------
print("eoo")
from hcsr04 import HCSR04
import time
sensor = HCSR04(trigger_pin=5, echo_pin=18, echo_timeout_us=10000)
# run = True
# while run:
#     distance =sensor.distance_cm()
#     print(distance)
#     if distance < 2:
#         run = False
#         print('GOL')
print("działa")
