# https://www.mutopiaproject.org/cgibin/make-table.cgi?collection=bachis&preview=1
from BasicScreenControl import BasicScreenControl
from mido.ports import BaseOutput
from mido import MidiFile
from rtmidi.midiutil import open_midioutput
from rtmidi.midiutil import open_midiinput

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
        print(self.midiInput.get_message())


class BasicMidiOut:

    def __init__(self, midiPort=1):
        self.midiout, self.port_name = open_midioutput(midiPort)
        print('On port name ', self.port_name)

    def sendMidi(self, note, velocity=112, command=0x90):
        self.midiout.send_message(
            [command, note, velocity])


class TestMidi(BasicMidiOut):
    lastNote = False

    def __init__(self):
        self.screen = BasicScreenControl()
        #self.MidiInClass = BasicMidiIn()
        super().__init__()

    def playNotesLoop(self):
        self.MidiInClass.checkForMidiMssg()
        self.tfReader = TFLuna()
        baseNote = 50
        while True:
            # middle c
            if(self.lastNote):
                pass
                # self.sendMidi(self.lastNote, 112, True)
    # math.ceil(
            time.sleep(.31)
            self.lastNote = min(
                75,  baseNote + self.tfReader.currentDist / 4)
            self.sendMidi(
                self.lastNote, 100, 0x90)
            self.screen.updateText(
                "Dist CM :" + str(self.tfReader.currentDist),

                "Current Note " + str(self.lastNote))
            # print(self.lastNote)
            time.sleep(1)


TestMidi().playNotesLoop()
