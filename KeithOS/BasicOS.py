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
    avaliblePrograms = ['Touch Basic', 'Touch Pro', 'Touch 3','Touch 4', 'Touch 5']
    def __init__(self):
        print('Start Midi OS ')
        self.inProgram = False
        self.screen = BasicScreenControl()
        self.button19 = Button(19)
        self.rotaryReadInstance = RotaryRead()
        self.rotaryReadInstance.runDial()
        midiPort = 2
        self.midiout, self.port_name = open_midioutput(midiPort)
        print('On port name ', self.port_name)

        try:
            self.tfReader = TFLuna()
        except print(0):
            self.tfReader = False
        self.runOS()
    @property
    def currentMenuItem(self):
        try:
              index = math.floor((self.rotaryReadInstance.rotateValue + 20) / 10 )
              return index
        except print(0):
                0
        #return self.avaliblePrograms[math.floor((self.rotaryReadInstance.rotateValue + 20) / 10 ) ]
    def runOS(self):
        screenThread = threading.Thread(target=self.basicOSscreen)
        screenThread.start()

    def killCommand(self):
        self.inProgram = False
    def basicOSscreen(self):
        
        while True: 
            time.sleep(.1)
            if self.inProgram:
                return
            currentSelectionText =    self.avaliblePrograms[self.currentMenuItem]
            self.screen.updateText(
                "Keith Midi OS", self.screen.getIP(), 'Click To start ',  currentSelectionText )
            if self.button19.is_pressed:
                self.inProgram = True
                TFMidi(self.screen, self.button19,
                     self.rotaryReadInstance,self.tfReader, self.midiout).runScreen()


#BasicOS().runOS()
