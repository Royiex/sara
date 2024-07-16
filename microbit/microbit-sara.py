def A():
    basic.clear_screen()
    basic.show_string("Hau ar ju")

def on_button_pressed_a():
    global state
    state = 2
    A()
    state = 1
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_gesture_tilt_left():
    global state
    basic.show_string("Haj puki Sawa")
    state = 1
input.on_gesture(Gesture.TILT_LEFT, on_gesture_tilt_left)

def B():
    basic.clear_screen()
    basic.show_string("I")
    basic.show_icon(IconNames.SMALL_HEART)
    basic.clear_screen()
    basic.show_string("Sara")
def Shake():
    basic.clear_screen()
    basic.show_string("Baj puki  Lav ju")

def on_button_pressed_b():
    global state
    state = 2
    B()
    state = 1
input.on_button_pressed(Button.B, on_button_pressed_b)

def on_gesture_shake():
    global state
    state = 2
    Shake()
    state = 0
    while state == 0:
        basic.show_leds("""
            . . . . .
            . . . . .
            . . . . .
            . . . . .
            . . . . .
            """)
input.on_gesture(Gesture.SHAKE, on_gesture_shake)

state = 0
basic.show_string("Haj puki Sawa")
state = 1

def on_forever():
    while state == 1:
        basic.show_icon(IconNames.HEART)
basic.forever(on_forever)
