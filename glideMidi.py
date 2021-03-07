# https://www.mutopiaproject.org/cgibin/make-table.cgi?collection=bachis&preview=1
from BasicScreenControl import BasicScreenControl
from mido.ports import BaseOutput
from mido import MidiFile
from rtmidi.midiutil import open_midioutput
import os
import mido
import time
import random
from Inputs.TFLuna import TFLuna

import math


class BasicMidiOut:
    lastNote = False

    def __init__(self):
        self.midiout, self.port_name = open_midioutput(1)
        self.screen = BasicScreenControl()

    def sendMidi(self, note, velocity=112, command=0x90):

        self.midiout.send_message(
            [command, note, velocity])

 #   if(message.type == 'note_off'):

  #      midiout.send_message(
   #         [0x80, message.note, message.velocity])
    def playNotesLoop(self):
        self.tfReader = TFLuna()
        baseNote = 50
        while True:
            # middle c
            if(self.lastNote):
                pass
                #self.sendMidi(self.lastNote, 112, True)

            time.sleep(.31)
            self.lastNote = min(
                75,  baseNote + math.ceil(self.tfReader.currentDist / 4))
            self.sendMidi(
                self.lastNote, 100, 0x90)
            self.screen.updateText(
                "Dist CM :" + str(self.tfReader.currentDist),

                "Current Note " + str(self.lastNote))
            # print(self.lastNote)
            time.sleep(1)


BasicMidiOut().playNotesLoop()
