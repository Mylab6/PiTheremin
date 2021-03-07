# https://www.mutopiaproject.org/cgibin/make-table.cgi?collection=bachis&preview=1
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

    def sendMidi(self, note, velocity=112, command=0x90):

        self.midiout.send_message(
            [command, note, velocity])

 #   if(message.type == 'note_off'):

  #      midiout.send_message(
   #         [0x80, message.note, message.velocity])
    def playNotesLoop(self):
        self.tfReader = TFLuna()
        baseNote = 60
        while True:
            # middle c
            if(self.lastNote):
                pass
                #self.sendMidi(self.lastNote, 112, True)

            time.sleep(.31)
            self.lastNote = max(
                68,  baseNote + math.ceil(self.tfReader.currentDist / 4))
            self.sendMidi(
                self.lastNote, 112, 0xE0)
            time.sleep(0.3)


BasicMidiOut().playNotesLoop()
