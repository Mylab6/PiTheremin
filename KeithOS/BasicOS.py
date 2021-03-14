from KeithOS.BasicScreenControl import BasicScreenControl
from KeithOS.Inputs.RotaryRead import RotaryRead
from rtmidi.midiutil import open_midioutput
from rtmidi.midiutil import open_midiinput
import sys
#sys.path.append('..')
# https://www.mutopiaproject.org/cgibin/make-table.cgi?collection=bachis&preview=1

import subprocess
from KeithOS.Instruments.TFMidi import TFMidi
import threading

import os
import mido
import time
import random
from KeithOS.Inputs.TFLuna import TFLuna

import math
from gpiozero import Button


class BasicOS:
    def __init__(self):
        print('Start Midi OS ')
        self.inProgram = False
        self.screen = BasicScreenControl()
        self.button19 = Button(19)
        self.rotaryReadInstance = RotaryRead()
        self.rotaryReadInstance.runDial()
        midiPort = 1
        self.midiout, self.port_name = open_midioutput(midiPort)
        print('On port name ', self.port_name)

        try:
            self.tfReader = TFLuna()
        except print(0):
            self.tfReader = False
        self.runOS()

    def runOS(self):
        screenThread = threading.Thread(target=self.basicOSscreen)
        screenThread.start()

    def basicOSscreen(self):
        
        while True: 
            time.sleep(.1)
            if self.inProgram:
                return
            self.screen.updateText(
                "Keith Midi OS", self.screen.getIP(), 'Click To start ')
            if self.button19.is_pressed:
                self.inProgram = True
                TFMidi(self.screen, self.button19,
                     self.rotaryReadInstance,self.tfReader, self.midiout, self).runScreen()


#BasicOS().runOS()
