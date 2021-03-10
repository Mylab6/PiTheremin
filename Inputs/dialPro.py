
import RPi.GPIO as GPIO
import threading
from time import sleep

# GPIO Ports
Enc_A = 20  				# Encoder input A: input GPIO 4
Enc_B = 26  			        # Encoder input B: input GPIO 14

Rotary_counter = 0  			# Start counting from 0
Current_A = 1					# Assume that rotary switch is not
Current_B = 1					# moving while we init software

LockRotary = threading.Lock()		# create lock for rotary switch


# initialize interrupt handlers
def init():
    GPIO.setwarnings(True)
    GPIO.setmode(GPIO.BCM)					# Use BCM mode
    # define the Encoder switch inputs
    GPIO.setup(Enc_A, GPIO.IN)
    GPIO.setup(Enc_B, GPIO.IN)
    # setup callback thread for the A and B encoder
    # use interrupts for all inputs
    GPIO.add_event_detect(Enc_A, GPIO.RISING,
                          callback=rotary_interrupt) 				# NO bouncetime
    GPIO.add_event_detect(Enc_B, GPIO.RISING,
                          callback=rotary_interrupt) 				# NO bouncetime
    return


# Rotarty encoder interrupt:
# this one is called for both inputs from rotary switch (A and B)
def rotary_interrupt(A_or_B):
    global Rotary_counter, Current_A, Current_B, LockRotary
    # read both of the switches
    Switch_A = GPIO.input(Enc_A)
    Switch_B = GPIO.input(Enc_B)
    # now check if state of A or B has changed
    # if not that means that bouncing caused it
    # Same interrupt as before (Bouncing)?
    if Current_A == Switch_A and Current_B == Switch_B:
        return										# ignore interrupt!

    Current_A = Switch_A								# remember new state
    Current_B = Switch_B								# for next bouncing check

    if (Switch_A and Switch_B):						# Both one active? Yes -> end of sequence
        LockRotary.acquire()						# get lock
        if A_or_B == Enc_B:							# Turning direction depends on
            Rotary_counter += 1						# which input gave last interrupt
        else:										# so depending on direction either
            Rotary_counter -= 1						# increase or decrease counter
        LockRotary.release()						# and release lock
    return											# THAT'S IT

# Main loop. Demonstrate reading, direction and speed of turning left/rignt


def main():
    global Rotary_counter, LockRotary

    Volume = 0									# Current Volume
    NewCounter = 0								# for faster reading with locks

    init()										# Init interrupts, GPIO, ...

    while True:								# start test
        sleep(0.1)								# sleep 100 msec

        # because of threading make sure no thread
        # changes value until we get them
        # and reset them

        LockRotary.acquire()					# get lock for rotary switch
        NewCounter = Rotary_counter			# get counter value
        Rotary_counter = 0						# RESET IT TO 0
        LockRotary.release()					# and release lock

        if (NewCounter != 0):					# Counter has CHANGED
            # Decrease or increase volume
            Volume = Volume + NewCounter*abs(NewCounter)
            if Volume < 0:						# limit volume to 0...100
                Volume = 0
            if Volume > 100:					# limit volume to 0...100
                Volume = 100
            print(NewCounter, Volume) 			# some test print


# start main demo function
main()
