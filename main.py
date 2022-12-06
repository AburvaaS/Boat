def on_button_pressed_a():
    servos.set_servo_position(servos.ServoPin.P1, Position.UP)
    servos.turn_servo(servos.ServoPin.P1, 45)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_ab():
    servos.reset_servos(servos.ServoPin.P0)
    servos.reset_servos(servos.ServoPin.P1)
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def on_button_pressed_b():
    servos.set_servo_position(servos.ServoPin.P0, Position.UP)
    servos.turn_servo(servos.ServoPin.P0, 45)
input.on_button_pressed(Button.B, on_button_pressed_b)

if touch.get_touch(touch.TouchPin.P12):
    pump.stop(Pump.LEFT)
    pump.stop(Pump.RIGHT)

def on_in_background():
    pump.start(Pump.LEFT, 100)
    pump.start(Pump.RIGHT, 100)
control.in_background(on_in_background)
