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
    def __init__(self):
        self.midiout, self.port_name = open_midioutput(1)

    def sendMidi(self, note, velocity=112):

        self.midiout.send_message(
            [0x90, note, velocity])
 #   if(message.type == 'note_off'):

  #      midiout.send_message(
   #         [0x80, message.note, message.velocity])
    def playNotesLoop(self):
        self.tfReader = TFLuna()
        while True:
            # middle c
            baseNote = 50

            self.sendMidi(
                max(68,  baseNote + math.ceil(self.tfReader.currentDist / 2)))
            time.sleep(.05)


BasicMidiOut().playNotesLoop()
