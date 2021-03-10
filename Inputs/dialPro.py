
import RPi.GPIO as GPIO
import threading
from time import sleep
from gpiozero import Button


class RotaryRead:
    # GPIO Ports
    Enc_A = 20  # CLK
    Enc_B = 26  # DT
    button = Button(19)  # SW
    rotateValue = 0
    Rotary_counter = 0  			# Start counting from 0
    Current_A = 1					# Assume that rotary switch is not
    Current_B = 1					# moving while we init software
    LockRotary = threading.Lock()		# create lock for rotary switch

    def init(self):
        GPIO.setwarnings(True)
        GPIO.setmode(GPIO.BCM)					# Use BCM mode
        GPIO.setup(self.Enc_A, GPIO.IN)
        GPIO.setup(self.Enc_B, GPIO.IN)

        GPIO.add_event_detect(self.Enc_A, GPIO.RISING,
                              callback=self.rotary_interrupt) 				# NO bouncetime
        GPIO.add_event_detect(self.Enc_B, GPIO.RISING,
                              callback=self.rotary_interrupt) 				# NO bouncetime

        return

    def rotary_interrupt(self, A_or_B):

        Switch_A = GPIO.input(self.Enc_A)
        Switch_B = GPIO.input(self.Enc_B)

        if self.Current_A == Switch_A and self.Current_B == Switch_B:
            return										# ignore interrupt!

        self.Current_A = Switch_A								# remember new state
        self.Current_B = Switch_B								# for next bouncing check

        if (Switch_A and Switch_B):						# Both one active? Yes -> end of sequence
            self.LockRotary.acquire()						# get lock
            if A_or_B == self.Enc_B:							# Turning direction depends on
                self.Rotary_counter += 1						# which input gave last interrupt
            else:										# so depending on direction either
                self.Rotary_counter -= 1						# increase or decrease counter
            self.LockRotary.release()						# and release lock
        return											# THAT'S IT

    def rotaryRead(self):
        #global Rotary_counter, LockRotary

        self.rotateValue = 0									# Current Volume
        NewCounter = 0								# for faster reading with locks

        self.init()										# Init interrupts, GPIO, ...

        while True:								# start test
            sleep(0.1)								# sleep 100 msec

        # because of threading make sure no thread
        # changes value until we get them
        # and reset them

            self.LockRotary.acquire()					# get lock for rotary switch
            NewCounter = self.Rotary_counter			# get counter value
            self.Rotary_counter = 0						# RESET IT TO 0
            self.LockRotary.release()					# and release lock

            if (NewCounter != 0):					# Counter has CHANGED
                # Decrease or increase volume
                self.rotateValue = self.rotateValue + \
                    NewCounter*abs(NewCounter)
                if self.rotateValue < 0:						# limit volume to 0...100
                    self.rotateValue = 0
                if self.rotateValue > 100:					# limit volume to 0...100
                    self.rotateValue = 100
                # print(NewCounter, self.rotateValue) 			# some test print

    def runDial(self):
        rotaryThread = threading.Thread(target=self.rotaryRead)
        rotaryThread.start()


rotaryReadInstance = RotaryRead().runDial()

while True:
    sleep(0.1)
    print(rotaryReadInstance.rotateValue)
    if rotaryReadInstance.button.is_pressed:
        print("Button is pressed")
