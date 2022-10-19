input.onButtonPressed(Button.A, function () {
    while (Servo2 <= 58) {
        Servo2 += 1
        pins.servoWritePin(AnalogPin.P2, Servo2)
        basic.pause(20)
    }
})
input.onButtonPressed(Button.AB, function () {
    while (Servo1 > -30) {
        Servo1 += -1
        pins.servoWritePin(AnalogPin.P1, Servo1)
        basic.pause(20)
    }
})
input.onButtonPressed(Button.B, function () {
    while (Servo2 >= 20) {
        Servo2 += -1
        pins.servoWritePin(AnalogPin.P2, Servo2)
        basic.pause(20)
    }
})
input.onGesture(Gesture.Shake, function () {
    while (Servo1 <= 210) {
        Servo1 += 1
        pins.servoWritePin(AnalogPin.P1, Servo1)
        basic.pause(20)
    }
})
let Servo2 = 0
let Servo1 = 0
pins.servoWritePin(AnalogPin.P0, 90)
pins.servoWritePin(AnalogPin.P1, 90)
pins.servoWritePin(AnalogPin.P2, 60)
let Servo0 = 90
Servo1 = 90
Servo2 = 60
basic.forever(function () {
	
})
