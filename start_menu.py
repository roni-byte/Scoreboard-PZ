from machine import Pin, SoftI2C, ADC
import SSD1306_OLED
import time


i2c = SoftI2C(scl=Pin(22), sda=Pin(21))

oled_width = 128
oled_height = 64
oled = SSD1306_OLED.SSD1306_I2C(oled_width, oled_height, i2c)


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


def where_is_joystick():
    x_center = 1872
    y_center = 1515
    x = ADC(Pin(15, Pin.IN))
    y = ADC(Pin(2, Pin.IN))
    x.atten(ADC.ATTN_11DB)
    y.atten(ADC.ATTN_11DB)

    # print(f'Current position: {x_val}, {y_val}')
    x_val = x.read()
    y_val = y.read()
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


def pick_left_or_right(height):
    last_placement = ''
    while True:
        placement = where_is_joystick()
        if (placement == 'left'):
            oled.fill_rect(0, height, 128, 60, 0)
            oled.text('_____', 10, height-6)
            oled.show()
            last_placement = placement
        elif (placement == 'right'):
            oled.fill_rect(0, height, 128, 60, 0)
            oled.text('_____', 75, height-6)
            oled.show()
            last_placement = placement
        if (placement == 'down'):
            if (last_placement == 'left'):
                return 'left'
            elif (last_placement == 'right'):
                return 'right'
            else:
                oled.text('you need to pick!', 0, 53)
                oled.show()
                time.sleep_ms(1000)
                oled.fill_rect(0, height, 128, 60, 0)
                oled.show()
        time.sleep_ms(1000)


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


def game_mode():
    points = 3
    rounds = 3
    clear_screen()
    oled.text('  GAME MODE', 20, 0)
    oled.text('POINTS:  3', 20, 15)
    oled.text('ROUNDS:  3', 20, 25)
    oled.text('EXIT', 20, 35)
    start_pos_of_pic_rec()
    oled.show()
    last_pos = 0
    while True:
        position = pick_up_or_down(last_pos, 3)
        last_pos = position
        if (position == 0):
            if (points == 9):
                points = 1
            else:
                points += 1
            oled.fill_rect(80, 15, 20, 10, 0)
            oled.text(str(points), 91, 15)
            oled.show()
            time.sleep_ms(500)
        elif (position == 1):
            if (rounds == 9):
                rounds = 1
            else:
                rounds += 1
            oled.fill_rect(80, 25, 20, 10, 0)
            oled.text(str(rounds), 91, 25)
            oled.show()
            time.sleep_ms(500)
        elif (position == 2):
            menu()


def settings():
    is_music_on = True
    are_sounds_on = True
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
            is_music_on = not is_music_on
            oled.fill_rect(80, 15, 30, 10, 0)
            if (is_music_on):
                oled.text('ON', 84, 15)
                time.sleep_ms(500)
            else:
                oled.text('OFF', 84, 15)
                time.sleep_ms(500)
            oled.show()
        elif (position == 1):
            are_sounds_on = not are_sounds_on
            oled.fill_rect(80, 25, 30, 10, 0)
            if (are_sounds_on):
                oled.text('ON', 84, 25)
                time.sleep_ms(500)
            else:
                oled.text('OFF', 84, 25)
                time.sleep_ms(500)
            oled.show()
        elif (position == 2):
            menu()


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
        game_mode()
    elif (position == 1):
        settings()
    elif (position == 2):
        show_rules()
    elif (position == 3):
        show_credits()
    elif (position == 4):
        show_beginning_screen()
    time.sleep_ms(7000)


def start_game():
    clear_screen()
    oled.text('READY ?', 40, 20)
    oled.text('  YES      NO', 0, 40)
    oled.show()
    time.sleep_ms(300)
    direction = pick_left_or_right(48)
    if (direction == 'left'):
        clear_screen()
        oled.text('START', 40, 0)
        oled.text('IN', 50, 10)
        oled.show()
        time.sleep_ms(300)
        for i in range(4, 0, -1):
            oled.fill_rect(0, 40, 128, 60, 0)
            oled.text(str(i), 55, 40)
            oled.show()
            time.sleep_ms(1000)
        clear_screen()
        oled.text('GO !!', 40, 20)
        oled.show()
        time.sleep_ms(500)
    else:
        show_beginning_screen()


def show_beginning_screen():
    clear_screen()
    oled.text('CAR SOCCER', 25, 0)
    oled.text(' -------------- ', 0, 6)
    oled.text(' use joystick:', 0, 11)
    oled.text(' L/R to pick', 0, 20)
    oled.text(' Down to select', 0, 28)
    oled.text(' -------------- ', 0, 36)

    oled.text('START   MENU', 10, 45)
    oled.show()

    direction = pick_left_or_right(53)
    if (direction == 'left'):
        start_game()
    else:
        menu_warning()
        menu()


# oled.pixel(0, 0, 1)
# oled.show()

# oled.invert(True)

# game_logo()
show_beginning_screen()

# game_mode()
# settings()
clear_screen()
