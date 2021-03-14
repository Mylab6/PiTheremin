import sys
#sys.path.append('..')
# https://www.mutopiaproject.org/cgibin/make-table.cgi?collection=bachis&preview=1
from BasicScreenControl import BasicScreenControl

from Inputs.RotaryRead import RotaryRead
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
        self.inProgram = False
        self.screen = BasicScreenControl()
        self.button19 = Button(19)
        self.rotaryReadInstance = RotaryRead()
        self.rotaryReadInstance.runDial()
        try:
            self.tfReader = TFLuna()
        except print(0):
            self.tfReader = False

    def runOS(self):
        screenThread = threading.Thread(target=self.basicOSscreen)
        screenThread.start()

    def basicOSscreen(self):
        if self.inProgram:
            return
        self.screen.updateText(
            "Keith Midi OS", self.screen.getIP(), 'Click To start ')
        if self.button19.is_pressed:
            self.inProgram = True
            TFMidi(self.screen, self.button19,
                     self.rotaryReadInstance).runScreen()


BasicOS().runOS()
