import machine
import time

notes_dic = {'C6': 1047, 'CS6': 1109, 'D6': 1175, 'DS6': 1245, 'E6': 1319,
             'F6': 1397, 'FS6': 1480, 'G6': 1568, 'GS6': 1661, 'A6': 1760,
             'AS6': 1865, 'B6': 1976, 'C7': 2093, 'CS7': 2217, 'D7': 2349,
             'DS7': 2489, 'E7': 2637, 'F7': 2794, 'FS7': 2960, 'G7': 3136,
             'GS7': 3322, 'A7': 3520, 'AS7': 3729, 'B7': 3951, '0': 0}

buzzer = machine.Pin(21)
pwmBuz = machine.PWM(buzzer)


def play(buz_pin, notes, delay, active_duty=200):
    buz = machine.PWM(buz_pin)
    for note in notes:
        if (note == '0'):  # Special case for silence
            buz.duty(0)
            # print('SILENCE')
        else:
            buz.freq(notes_dic[note])
            buz.duty(active_duty)
        time.sleep_ms(delay)
    buz.duty(0)
    buz.deinit()
    return


# pwmBuz.freq(1397)
# time.sleep_ms(200)
# pwmBuz.freq(1047)
# time.sleep_ms(200)
# pwmBuz.duty(0)

def buzzing():
    for i in range(5):
        buzzer.value(1)
        time.sleep_ms(200)
        buzzer.value(0)
        time.sleep_ms(200)
    return


song = [
    'E7', 'E7',  '0', 'E7',  '0', 'C7', 'E7',  '0',
    'G7',  '0',  '0',  '0', 'G6',  '0',  '0',  '0',
    'C7',  '0',  '0', 'G6',  '0',  '0', 'E6',  '0',
    '0', 'A6',  '0', 'B6',  '0', 'AS6', 'A6',  '0',
    'G6', 'E7',  '0', 'G7', 'A7',  '0', 'F7', 'G7',
    '0', 'E7',  '0', 'C7', 'D7', 'B6',  '0',  '0',
    'C7',  '0',  '0', 'G6',  '0',  '0', 'E6',  '0',
    '0', 'A6',  '0', 'B6',  '0', 'AS6', 'A6',  '0',
    'G6', 'E7',  '0', 'G7', 'A7',  '0', 'F7', 'G7',
    '0', 'E7',  '0', 'C7', 'D7', 'B6',  '0',  '0',
]

win_song = [
    'FS6', 'FS6', 'DS7', 'E7', 'F7', '0', 'AS7', 'A7', 'AS7', 'A7', 'AS7', '0'
]

fail_song = [
    'D6', 'D6', 'D6', 'CS6', 'CS6', 'CS6', 'C6', 'C6', 'C6', 'C6', '0'
]

play(buzzer, song, 200)

pwmBuz.duty(0)
buzzer.value(0)
pwmBuz.deinit()
print('Done :)')


B0  = 31
C1  = 33
CS1 = 35
D1  = 37
DS1 = 39
E1  = 41
F1  = 44
FS1 = 46
G1  = 49
GS1 = 52
A1  = 55
AS1 = 58
B1  = 62
C2  = 65
CS2 = 69
D2  = 73
DS2 = 78
E2  = 82
F2  = 87
FS2 = 93
G2  = 98
GS2 = 104
A2  = 110
AS2 = 117
B2  = 123
C3  = 131
CS3 = 139
D3  = 147
DS3 = 156
E3  = 165
F3  = 175
FS3 = 185
G3  = 196
GS3 = 208
A3  = 220
AS3 = 233
B3  = 247
C4  = 262
CS4 = 277
D4  = 294
DS4 = 311
E4  = 330
F4  = 349
FS4 = 370
G4  = 392
GS4 = 415
A4  = 440
AS4 = 466
B4  = 494
C5  = 523
CS5 = 554
D5  = 587
DS5 = 622
E5  = 659
F5  = 698
FS5 = 740
G5  = 784
GS5 = 831
A5  = 880
AS5 = 932
B5  = 988
C6  = 1047
CS6 = 1109
D6  = 1175
DS6 = 1245
E6  = 1319
F6  = 1397
FS6 = 1480
G6  = 1568
GS6 = 1661
A6  = 1760
AS6 = 1865
B6  = 1976
C7  = 2093
CS7 = 2217
D7  = 2349
DS7 = 2489
E7  = 2637
F7  = 2794
FS7 = 2960
G7  = 3136
GS7 = 3322
A7  = 3520
AS7 = 3729
B7  = 3951
C8  = 4186
CS8 = 4435
D8  = 4699
DS8 = 4978


class Buzzer:
    def __init__(self, signed_pin):
		# Takes a number of assigned pin
        self.pwm = machine.PWM(Pin(signed_pin, Pin.OUT))

    def play(self, melody, wait, duty):
        for note in melody:
            self.pwm.freq(note)
            self.pwm.duty(duty)
            time.sleep(wait)
        self.pwm.duty(0) # turn off the buzzer

melody1 = [G7, 0, G7, 0, G7]
melody2 = [D5, 0, D5]
melody3 = [D2, 0, D2]
melody4 = [B6, 0, B6, 0, B6, B6, B6, 0, B6, B6, 0, B6, B6]


buzzer = Buzzer(15)
buzzer.play(melody1, 0.15, 50)

