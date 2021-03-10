from RPi import GPIO
from time import sleep

from gpiozero import Button
clk = 20
dt = 26

button = Button(19)
GPIO.setmode(GPIO.BCM)
GPIO.setup(clk, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(dt, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

counter = 0
clkLastState = GPIO.input(clk)

try:

    while True:
        if button.is_pressed:
            print("Button is pressed")
        clkState = GPIO.input(clk)
        dtState = GPIO.input(dt)
        if clkState != clkLastState:
            if dtState != clkState:
                counter += 1
            else:
                counter -= 1

        print(counter)
        clkLastState = clkState
        sleep(0.01)
finally:
    GPIO.cleanup()
