# https://www.mutopiaproject.org/cgibin/make-table.cgi?collection=bachis&preview=1
from BasicScreenControl import BasicScreenControl
from mido.ports import BaseOutput
from mido import MidiFile
from rtmidi.midiutil import open_midioutput
from rtmidi.midiutil import open_midiinput
from Inputs.dialPro import RotaryRead

import threading

import os
import mido
import time
import random
from Inputs.TFLuna import TFLuna

import math


class BasicMidiIn:

    def __init__(self, midiPort=1):
        self.midiInput, self.port_name = open_midiinput(midiPort)

    def checkForMidiMssg(self):
        msg = self.midiInput.get_message()


class BasicMidiOut:

    def __init__(self, midiPort=1):
        self.midiout, self.port_name = open_midioutput(midiPort)
        print('On port name ', self.port_name)

    def sendMidi(self, note, velocity, command):
        self.midiout.send_message(
            [command, note, velocity])

    def sendNoteOn(self, note, velocity=112):
        self.sendMidi(note, velocity, 0x90)

    def sendNoteOff(self, note, velocity=112):
        self.sendMidi(note, velocity, 0x80)


class TestMidi(BasicMidiOut):
    lastNote = False
    orignalNote = 58
    noteSpeed = 0

    @property
    def baseNote(self):
        return self.orignalNote + self.rotaryReadInstance.rotateValue

    def __init__(self):
        self.screen = BasicScreenControl()
        self.MidiInClass = BasicMidiIn()
        self.rotaryReadInstance = RotaryRead()
        self.rotaryReadInstance.runDial()
        self.tfReader = TFLuna()
        self.tfReader.SendNote = self.SendNote
        super().__init__()

    def updateScreen(self):

        while True:
            time.sleep(.5)
            self.screen.updateText(
                "Dist CM :" + str(self.tfReader.currentDist),

                "Current Note " +
                str(self.lastNote),  "Note Speed: " +
                str(self.noteSpeed), 'Base Note :' + str(self.baseNote)
            )

        # while True:
        #    self.SendNote()

    def SendNote(self, speed):
        self.noteSpeed = speed
        self.MidiInClass.checkForMidiMssg()

        if(self.lastNote):
            self.sendNoteOff(self.lastNote)

        # time.sleep(.31)
        self.lastNote = min(
            75,  self.baseNote + self.tfReader.currentDist / 4)

        if(speed > 60):
            self.sendNoteOn(
                self.lastNote)

        # time.sleep(1)
    def runScreen(self):
        screenThread = threading.Thread(target=self.updateScreen)
        screenThread.start()


TestMidi().runScreen()
