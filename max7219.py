from max7219 import Matrix8x8
from machine import Pin, SPI
from time import sleep

"""
How to connect:
VCC - 3V3/VIN
GND - GND
DIN - D23 (MOSI)
CS - D5 e.g
CLK - D18 (SCK)
"""

def max7219_configuration(sck_pin=18, mosi_pin=23, cs_pin=5) -> "Matrix8x8":
    """
    Configuratoin of max7219 with passed assigned pins.
    Defaults pins are equal to these at the beginning of the file
    """
    spi = SPI(1, baudrate=10000000, polarity=1, phase=0, sck=Pin(sck_pin), mosi=Pin(mosi_pin))
    ss = Pin(cs_pin, Pin.OUT)
    return Matrix8x8(spi, ss, 1) 

def max7219_show(matrix: "Matrix8x8", param):
    """
    Function takes an instance of class Matrix8x8 and parameter;
    Depending on parameter it shows:
    1 - number 1 
    2 - number 2
    3- number 3
    "left" - left arrow
    "right" - right arrow 
    """
    if param == 1 or param == 2 or param == 3:
        matrix.fill(0)  # clears the display
        matrix.text(str(param), 0, 0, 1)
        matrix.show()  # loads the display
    elif param == "left":
        matrix.fill(0)
        matrix.fill_rect(1, 2, 5, 5, 1)
        matrix.fill_rect(6, 3, 1, 3, 1)
        matrix.pixel(7, 4, 1)
        matrix.pixel(4, 1, 1)
        matrix.pixel(4, 7, 1)
        matrix.show()
    elif param == "right":
        matrix.fill(0)
        matrix.fill_rect(2, 2, 5, 5, 1)
        matrix.fill_rect(1, 3, 1, 3, 1)
        matrix.pixel(0, 4, 1)
        matrix.pixel(3, 1, 1)
        matrix.pixel(3, 7, 1)
        matrix.show()
    else:
        raise ValueError("No such argument, possible arguments: 1, 2, 3, 'left', 'right'")
    

def max7219_time_is_up(matrix: "Matrix8x8"):
    """
    Function takes an instance of class Matrix8x8
    and return a signal which informs about the end of
    the time
    """
    for _ in range(2):
        matrix.fill(0)
        n = 2
        k = 3
        for _ in range(4):
            sleep(0.5)
            matrix.fill_rect(k, k, n, n, 1)
            matrix.show()
            n += 2
            k -= 1
    for _ in range(2):
        matrix.fill(1)
        matrix.show()
        sleep(0.25)
        matrix.fill(0)
        matrix.show()
        sleep(0.25)


def max7219_show_functionalities(sck_pin=18, mosi_pin=23, cs_pin=5):
    """
    Basically shows every display that the function max7219 can show,
    Default pins assignments is as shown at the beginning of the file
    """
    display = max7219_configuration(sck_pin, mosi_pin, cs_pin)
    for _ in range(4):
        max7219_show(display, 1)
        sleep(2)
        max7219_show(display, 2)
        sleep(2)
        max7219_show(display, 3)
        sleep(2)
        max7219_show(display, "left")
        sleep(2)
        max7219_show(display, "right")
        sleep(2)


# display = max7219_configuration()
# max7219_time_is_up(display)

# max7219_show_functionalities()
