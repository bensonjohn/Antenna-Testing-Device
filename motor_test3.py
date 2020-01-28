from gpiozero import Button
from gpiozero import DigitalOutputDevice
from time import sleep

pin_a = Button(22)
pin_b = Button(23)
pin_z = Button(24)

device = DigitalOutputDevice(pin=17)

a = pin_a.is_pressed
b = pin_b.is_pressed

prev_a = not a
prev_b = not b
prev_z = True

counter = 0

loop = True
while(loop):
	device.on()
	sleep(.001)
	device.off()
	sleep(.001)
	if a != pin_a.is_pressed or b != pin_b.is_pressed:
		if pin_a.is_pressed == prev_a and pin_b.is_pressed == prev_b:
			counter -= 1
		else:
			counter += 1
		print(str(pin_a.is_pressed) + " " + str(pin_b.is_pressed) + " " + str(pin_z.is_pressed) + " " + str(counter))
		a = pin_a.is_pressed
		prev_a = a
		b = pin_b.is_pressed
		prev_b = b
	loop = pin_z.is_pressed or prev_z
	prev_z = pin_z.is_pressed
device.off()
