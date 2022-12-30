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
