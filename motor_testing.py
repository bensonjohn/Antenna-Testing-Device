import state_machine
from gpiozero import Button
from gpiozero import DigitalOutputDevice
from time import sleep

pin_a = Button(22)
pin_b = Button(23)
pin_z = Button(24)

device = DigitalOutputDevice(pin=17)

a = pin_a.is_pressed
b = pin_b.is_pressed
z = pin_z.is_pressed

counter = 0

# amount of increments for a full rotation of geared motor shaft with a gear ratio of ~26.85:1
# assuming increments for one rotation is 4000
# full_rotation = 107405

delay = .001

fsm = state_machine.Motor_State_Machine()
fsm.update(state_machine.Motor_State.s0, a, b, z, start=True, stop=False, pause=False)
up_down = False
count_enable = False
no_error = True
at_zero = False
prev_at_zero = False
revolutions = 1
errors = 0
while(revolutions > 0):
    device.on()
    sleep(delay)
    device.off()
    sleep(delay)
    up_down, count_enable, no_error, at_zero = fsm.update(fsm.future_state, pin_a.is_pressed, pin_b.is_pressed, pin_z.is_pressed, start=True, stop=False, pause=False)
    if at_zero and prev_at_zero:
        revolutions -= 1
    if not no_error:
        errors += 1
    if not count_enable:
        if up_down:
            counter -= 1
        else:
            counter += 1
    prev_at_zero = at_zero
    print(str(fsm.future_state)+ " " + str(int(pin_a.is_pressed)) + " " + str(int(pin_b.is_pressed)) + " " + str(int(pin_z.is_pressed)) + " " + str(counter))
print("Errors: " + str(errors))
device.off()
