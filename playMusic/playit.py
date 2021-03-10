# https://www.mutopiaproject.org/cgibin/make-table.cgi?collection=bachis&preview=1
from mido.ports import BaseOutput
from mido import MidiFile
from rtmidi.midiutil import open_midioutput
import os
import mido
import random
from playsound import playsound

dn = os.path.dirname(os.path.realpath(__file__))

midiPath = os.path.join(dn, 'music')
midis = os.listdir(midiPath)
# print(midis)
music = os.path.join(midiPath, random.choice(midis))
print('Playing ', music)
playsound(music)
