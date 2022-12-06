input.onButtonPressed(Button.A, function () {
    x = 45
    servos.setServoPosition(servos.ServoPin.P1, Position.UP)
    servos.turnServo(servos.ServoPin.P1, x)
})
input.onButtonPressed(Button.B, function () {
    x = 45
    servos.setServoPosition(servos.ServoPin.P0, Position.UP)
    servos.turnServo(servos.ServoPin.P0, x)
})
let x = 0
if (touch.getTouch(touch.TouchPin.P12)) {
    pump.start(Pump.LEFT, 100)
    pump.start(Pump.RIGHT, 100)
}
if (touch.getTouch(touch.TouchPin.P0)) {
    pump.stop(Pump.LEFT)
    pump.stop(Pump.RIGHT)
}
loops.everyInterval(2000, function () {
    x = 0
    servos.resetServos(servos.ServoPin.P0)
    servos.resetServos(servos.ServoPin.P1)
})
