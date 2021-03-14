# https://www.mutopiaproject.org/cgibin/make-table.cgi?collection=bachis&preview=1
from BasicScreenControl import BasicScreenControl
from mido.ports import BaseOutput
from mido import MidiFile
from rtmidi.midiutil import open_midioutput
from rtmidi.midiutil import open_midiinput
from Inputs.dialPro import RotaryRead
import subprocess
from glideMidi import TestMidi
import threading

import os
import mido
import time
import random
from Inputs.TFLuna import TFLuna

import math
from gpiozero import Button
from KeithOS.BasicControllableItem import BasicControllableItem


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
        screenThread = threading.Thread(target=self.updateScreen)
        screenThread.start()

    def basicOSscreen(self):
        if self.inProgram:
            return
        self.screen.updateText(
            "Keith Midi OS", self.screen.getIP(), 'Click To start ')
        if self.button19.is_pressed:
            self.inProgram = True
            TestMidi(self.screen, self.button19,
                     self.rotaryReadInstance).runScreen()
