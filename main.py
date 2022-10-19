def on_button_pressed_a():
    global Servo2
    while Servo2 <= 58:
        Servo2 += 1
        pins.servo_write_pin(AnalogPin.P2, Servo2)
        basic.pause(20)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_ab():
    global Servo1
    while Servo1 > -30:
        Servo1 += -1
        pins.servo_write_pin(AnalogPin.P1, Servo1)
        basic.pause(20)
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def on_button_pressed_b():
    global Servo2
    while Servo2 >= 20:
        Servo2 += -1
        pins.servo_write_pin(AnalogPin.P2, Servo2)
        basic.pause(20)
input.on_button_pressed(Button.B, on_button_pressed_b)

def on_gesture_shake():
    global Servo1
    while Servo1 <= 210:
        Servo1 += 1
        pins.servo_write_pin(AnalogPin.P1, Servo1)
        basic.pause(20)
input.on_gesture(Gesture.SHAKE, on_gesture_shake)

Servo2 = 0
Servo1 = 0
pins.servo_write_pin(AnalogPin.P0, 90)
pins.servo_write_pin(AnalogPin.P1, 90)
pins.servo_write_pin(AnalogPin.P2, 60)
Servo0 = 90
Servo1 = 90
Servo2 = 60

def on_forever():
    pass
basic.forever(on_forever)
