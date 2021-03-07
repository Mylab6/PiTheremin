import logging
import sys
import time
from os.path import exists

from gpiozero import LED, Button
import rtmidi
from rtmidi.midiutil import open_midioutput
from rtmidi.midiconstants import (
    NOTE_OFF,
    NOTE_ON,
    POLYPHONIC_PRESSURE,
    CONTROLLER_CHANGE,
    PROGRAM_CHANGE,
    CHANNEL_PRESSURE,
    PITCH_BEND
)

# /home/pi/PiMidi/keithMidi.py


def main():
    logging.basicConfig(
        format="%(name)s: %(levelname)s - %(message)s", level=logging.INFO)

    midiout, port_name = open_midioutput(1)

    print("Entering main loop. Press Control-C to exit.")

    try:
        while True:
            note_on = [0x90, 60, 112]  # channel 1, middle C, velocity 112
            note_off = [0x80, 60, 0]
            midiout.send_message(note_on)
            time.sleep(0.5)
            midiout.send_message(note_off)
            time.sleep(0.1)

          # Hold behaviour (Press=ON, Release=OFF)
          # footcontroller.btn4.when_pressed = lambda : footcontroller.sendMIDI(type=CONTROLLER_CHANGE, channel=0x40, value=64)
          # footcontroller.btn4.when_released = lambda : footcontroller.sendMIDI(type=CONTROLLER_CHANGE, channel=0x40, value=0)

          # Toggle behaviour (Press=ON, Press again=OFF)
          # footcontroller.btn5.when_pressed = lambda : footcontroller.sendMIDI(type=CONTROLLER_CHANGE, channel=0x50)

          # Usually free MIDI Channels:
          # 0x50, 0x51, 0x52, 0x53, 0x55, 0X56, 0X57, 0X59, 0X5A,
          # 0X66, 0X67, 0X68, 0X69, 0X6A, 0X6B, 0X6C, 0X6D, 0X6E,
          # 0X6F, 0X70, 0X71, 0X72, 0X73, 0X74, 0X75, 0X76, 0X77

    except KeyboardInterrupt:
        print('')
    finally:
        #del footcontroller
        del midiout


if __name__ == '__main__':
    sys.exit(main())
