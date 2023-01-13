from machine import Pin, SoftI2C, ADC, mem32
import machine
import ssd1306
from play_game_hcsr04 import who_scored
from oled1306 import show_single_number, oled1306_print_result
import buzzer_sounds
import byte_arrays
import time
import leds
# import stm32lib

i2c = SoftI2C(scl=Pin(22), sda=Pin(21))

oled_width = 128
oled_height = 64
oled = ssd1306.SSD1306_I2C(oled_width, oled_height, i2c)
buzzer = buzzer_sounds.Buzzer(32)
num_buffors = [
    byte_arrays.buffer_0, byte_arrays.buffer_1, byte_arrays.buffer_2, byte_arrays.buffer_3, byte_arrays.buffer_4,
    byte_arrays.buffer_5, byte_arrays.buffer_6, byte_arrays.buffer_7, byte_arrays.buffer_8, byte_arrays.buffer_9
              ]


def clear_screen():
    time.sleep_ms(10)
    oled.invert(False)
    oled.fill(0)  # make all pixels black
    oled.show()
    time.sleep_ms(10)
    return


def game_logo():
    clear_screen()
    for i in range(-30, 135):
        oled.fill(0)
        oled.text('CAR', i, 0)
        oled.text('SOCCER', 128 - 40 - i, 16)
        oled.show()
        if (i == 45):
            oled.text('by', 50, 32)
            oled.text(' Tedium Busters', 0, 48)
            oled.show()
            time.sleep_ms(1500)
    clear_screen()


def disableADC():
    # mem32[0x3FF4880C] &= 0xFFF3FFFF
    # mem32[0x3FF4880C] |= 0x00020000
    mem32[0x3FF4880C] = 0


def where_is_joystick():
    x_center = 1872
    y_center = 1515
    # adc = machine.ADC(Pin(2))
    # apin = ADC.channel(pin='GPIO2')
    x = ADC(Pin(15, Pin.IN))
    y = ADC(Pin(2, Pin.IN))
    # y = apin
    x.atten(ADC.ATTN_11DB)
    y.atten(ADC.ATTN_11DB)

    # print(f'Current position: {x_val}, {y_val}')
    x_val = x.read()
    y_val = y.read()
    x = ADC(0)
    y = ADC(0)

    # adc.deinit()
    # disableADC()
    if (x_val < x_center - 10):
        # print('left')
        return 'left'
    elif (x_val > x_center + 10):
        # print('right')
        return 'right'

    if (y_val < y_center - 10):
        # print('up')
        return 'up'
    elif (y_val > y_center + 10):
        # print('down')
        return 'down'

    if (abs(x_val - x_center) <= 10 and abs(y_val - y_center) <= 10):
        # print('center')
        return 'center'


def picking_rect(height):
    oled.fill_rect(5, 0, 10, 64, 0)
    oled.show()
    oled.fill_rect(5, height, 10, 8, 1)
    oled.show()


def start_pos_of_pic_rec():
    picking_rect(13)


def pick_up_or_down(start_pos, max_position):
    position = start_pos
    while True:
        placement = where_is_joystick()
        if (placement == 'up'):
            if (position == 0):
                position = max_position-1
            else:
                position -= 1
            picking_rect(position*10+13)
        elif (placement == 'down'):
            if (position == max_position-1):
                position = 0
            else:
                position += 1
            picking_rect(position*10+13)
        elif (placement == 'right'):
            return position
        time.sleep_ms(1000)


def menu_warning():
    clear_screen()
    oled.text('!! WARNING !!', 10, 0)
    oled.text('IN MENU', 0, 10)
    oled.text('use joystick:', 0, 20)
    oled.text('Up/Down to pick', 6, 30)
    oled.text('Right to select', 6, 40)
    oled.text('!!!!', 40, 50)
    oled.show()
    time.sleep_ms(7000)
    clear_screen()


def show_credits():
    clear_screen()
    oled.text('Created by:', 0, 0)
    oled.text('TEDIUM', 30, 10)
    oled.text('BUSTERS', 30, 20)
    oled.text(' TEAM', 30, 30)
    oled.text('Thank you', 0, 40)
    oled.text(' for playing :)', 0, 50)
    oled.show()
    time.sleep_ms(4000)
    menu()


def show_rules():
    clear_screen()
    oled.text('Push ball with a', 0, 0)
    oled.text("car into enemy's", 0, 10)
    oled.text('gate. Score', 0, 20)
    oled.text('faster than', 0, 30)
    oled.text('enemy and win.', 0, 40)
    oled.text('Good luck!', 0, 53)
    oled.show()
    time.sleep_ms(6000)
    menu()


class Menu_options():
    def __init__(self, points, fights) -> None:
        self.is_music_on = True
        self.are_sounds_on = True
        self.points = points
        self.fights = fights

    # def play_sound(self):
        # if (self.are_sounds_on):
            # buzzer.play(buzzer_sounds.menu_sound, 200)

    def pick_left_or_right(self, height):
        last_placement = ''
        while True:
            placement = where_is_joystick()
            if (placement == 'left'):
                # buzzer.play(buzzer_sounds.win_song, 200)
                oled.fill_rect(0, height, 128, 60, 0)
                oled.text('_____', 10, height-6)
                oled.show()
                # if (self.are_sounds_on):
                # buzzer.play(buzzer_sounds.win_song, 200)
                # buzzer.play(buzzer_sounds.menu_sound, 200)
                # self.play_sound()
                last_placement = placement
            elif (placement == 'right'):
                oled.fill_rect(0, height, 128, 60, 0)
                oled.text('_____', 75, height-6)
                oled.show()
                # self.play_sound()
                last_placement = placement
            if (placement == 'down'):
                if (last_placement == 'left'):
                    # self.play_sound()
                    return 'left'
                elif (last_placement == 'right'):
                    # self.play_sound()
                    return 'right'
                else:
                    oled.text('you need to pick!', 0, 53)
                    oled.show()
                    # if (self.are_sounds_on):
                        # buzzer.play(buzzer_sounds.menu_wrong_sound, 200)
                    time.sleep_ms(1000)
                    oled.fill_rect(0, height, 128, 60, 0)
                    oled.show()
            time.sleep_ms(1000)

    def game_mode(self):
        clear_screen()
        oled.text('  GAME MODE', 20, 0)
        oled.text(f'POINTS:  {self.points}', 20, 15)
        oled.text(f'FIGHTS:  {self.fights}', 20, 25)
        oled.text('EXIT', 20, 35)
        start_pos_of_pic_rec()
        oled.show()
        last_pos = 0
        while True:
            position = pick_up_or_down(last_pos, 3)
            last_pos = position
            if (position == 0):
                if (self.points == 9):
                    self.points = 1
                else:
                    self.points += 1
                oled.fill_rect(80, 15, 20, 10, 0)
                oled.text(str(self.points), 91, 15)
                oled.show()
                time.sleep_ms(500)
            elif (position == 1):
                if (self.fights == 9):
                    self.fights = 1
                else:
                    self.fights += 1
                oled.fill_rect(80, 25, 20, 10, 0)
                oled.text(str(self.fights), 91, 25)
                oled.show()
                time.sleep_ms(500)
            elif (position == 2):
                menu()

    def settings(self):
        clear_screen()
        oled.text('  SETTINGS', 20, 0)
        oled.text('MUSIC:  ON', 20, 15)
        oled.text('SOUNDS: ON', 20, 25)
        oled.text('EXIT', 20, 35)
        start_pos_of_pic_rec()
        oled.show()
        last_pos = 0
        while True:
            position = pick_up_or_down(last_pos, 3)
            last_pos = position
            if (position == 0):
                self.is_music_on = not self.is_music_on
                oled.fill_rect(80, 15, 30, 10, 0)
                if (self.is_music_on):
                    oled.text('ON', 84, 15)
                    time.sleep_ms(500)
                else:
                    oled.text('OFF', 84, 15)
                    time.sleep_ms(500)
                oled.show()
            elif (position == 1):
                self.are_sounds_on = not self.are_sounds_on
                oled.fill_rect(80, 25, 30, 10, 0)
                if (self.are_sounds_on):
                    oled.text('ON', 84, 25)
                    time.sleep_ms(500)
                else:
                    oled.text('OFF', 84, 25)
                    time.sleep_ms(500)
                oled.show()
            elif (position == 2):
                menu()

    def start_game(self):
        clear_screen()
        # buzzer.play(buzzer_sounds.silence, 200)
        oled.text('READY ?', 40, 20)
        oled.text('  YES      NO', 0, 40)
        oled.show()
        time.sleep_ms(300)
        direction = menu_options.pick_left_or_right(48)
        if (direction == 'left'):
            clear_screen()
            oled.text('START', 40, 0)
            oled.text('IN', 50, 10)
            oled.show()
            time.sleep_ms(1000)
            leds_types = [leds.ledR, leds.ledY, leds.ledY]
            for i in range(3, 0, -1):
                show_single_number(oled, num_buffors[i])
                leds_types[i % 3].on()
                time.sleep_ms(1000)
                leds_types[i % 3].off()
                time.sleep_ms(1000)
            clear_screen()
            oled.text('GO !!', 40, 20)
            oled.show()
            leds.miga(leds.ledG, 1)
            time.sleep_ms(500)
            clear_screen()
            self.play_games(self.fights, self.points)
            time.sleep_ms(500)
        else:
            show_beginning_screen()

    def play_games(self, rounds, max_points):
        left = 0
        right = 0
        for i in range(rounds):
            round_winner = self.play_game(max_points)
            if (round_winner == 'left'):
                left += 1
            if (round_winner == 'right'):
                right += 1
            if (i < rounds-1):
                oled.text(f'FIGHT {i+2}', 30, 0)
                oled.text(' fights won:', 0, 20)
                oled.text(f'{left} : {right}', 30, 40)
                oled.show()
                time.sleep_ms(2000)
                clear_screen()

        clear_screen()
        # if (self.are_sounds_on):
            # buzzer.play(buzzer_sounds.win_song, 200)
        oled.text('GAME OVER', 20, 0)
        oled.text('Winner is player:', 0, 20)
        if (right > left):
            oled.text('on the RIGHT', 0, 40)
        if (left > right):
            oled.text('on the LEFT', 0, 40)
        if (left == right):
            oled.text('NONE you tied', 0, 40)
        oled.show()
        leds.flash_all_leds()
        time.sleep_ms(1000)
        leds.flash_all_leds()
        time.sleep_ms(5000)
        show_beginning_screen()

    def play_game(self, max_points):
        left = 0
        right = 0
        oled1306_print_result(oled, num_buffors[0], num_buffors[0])
        for i in range(max_points):
            scored_gate_pos = who_scored(left, right)

            # if button was pressed, add value and continue waiting for goal
            if (scored_gate_pos == 'left_button'):
                left += 1
                scored_gate_pos = who_scored(left, right)
            if (scored_gate_pos == 'right_button'):
                right += 1
                scored_gate_pos = who_scored(left, right)

            if (scored_gate_pos == 'left'):
                left += 1
            if (scored_gate_pos == 'right'):
                right += 1
            clear_screen()
            oled.text('GOAL !!', 40, 20)
            oled.show()
            # leds.miga(leds.ledY, 2)
            leds.flash_all_leds()
            time.sleep_ms(500)
            clear_screen()
            if (i < max_points-1):
                oled.text('ROUND', 40, 20)
                oled.text(str(i+2), 50, 40)
                oled.show()
            time.sleep_ms(500)
            oled1306_print_result(oled, num_buffors[left], num_buffors[right])
            time.sleep_ms(500)
        clear_screen()
        # if (self.are_sounds_on):
        # buzzer.play(buzzer_sounds.win_song, 200)
        oled.text('FIGHT OVER', 20, 0)
        oled.text('Fight won player:', 0, 20)
        if (right > left):
            oled.text('on the RIGHT', 0, 40)
            oled.show()
            leds.miga(leds.ledG, 2)
        if (left > right):
            oled.text('on the LEFT', 0, 40)
            oled.show()
            leds.miga(leds.ledR, 2)
        if (left == right):
            oled.text('NONE you tied', 0, 40)
            oled.show()
            leds.miga(leds.ledY, 2)
        time.sleep_ms(5000)
        clear_screen()
        if (right == max_points):
            return 'right'
        if (left == max_points):
            return 'left'
        else:
            return 'tie'

def menu():
    clear_screen()
    oled.text('  MENU', 20, 0)
    oled.text('GAME MODE', 20, 15)
    oled.text('SETTINGS', 20, 25)
    oled.text('RULES', 20, 35)
    oled.text('CREDITS', 20, 45)
    oled.text('EXIT', 20, 55)
    start_pos_of_pic_rec()
    oled.show()
    time.sleep_ms(500)
    position = pick_up_or_down(0, 5)
    if (position == 0):
        menu_options.game_mode()
    elif (position == 1):
        menu_options.settings()
    elif (position == 2):
        show_rules()
    elif (position == 3):
        show_credits()
    elif (position == 4):
        show_beginning_screen()
    time.sleep_ms(7000)



def show_beginning_screen():
    # buzzer.play(buzzer_sounds.melody4, 200)
    # buzzer.play(buzzer_sounds.silence, 200)
    clear_screen()
    oled.text('CAR SOCCER', 25, 0)
    oled.text(' -------------- ', 0, 6)
    oled.text(' use joystick:', 0, 11)
    oled.text(' L/R to pick', 0, 20)
    oled.text(' Down to select', 0, 28)
    oled.text(' -------------- ', 0, 36)

    oled.text('START   MENU', 10, 45)
    oled.show()

    direction = menu_options.pick_left_or_right(53)
    if (direction == 'left'):
        menu_options.start_game()
    else:
        menu_warning()
        menu()


# oled.pixel(0, 0, 1)
# oled.show()

# oled.invert(True)

# game_logo()
# play_game(3)
# game_mode()
# settings()

menu_options = Menu_options(2, 3)
# menu_options.start_game()
# show_beginning_screen()
# menu_options.play_game(3)
# buzzer.play(buzzer_sounds.silence, 200)
buzzer.play(buzzer_sounds.win_song, 200)
print(where_is_joystick())
buzzer.play(buzzer_sounds.win_song, 200)


clear_screen()
