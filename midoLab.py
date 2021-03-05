from mido.ports import BaseOutput
from mido import MidiFile
from rtmidi.midiutil import open_midioutput

import mido

import random

mid = MidiFile('midi.mid')
#port = PrintPort()
midiout, port_name = open_midioutput(1)
noteShift = random.randint(-2, 2)
for message in mid.play():
    # print(msg)
    # port.send(msg)
    if(message.type == 'note_on'):
        print('send note ON ')
        midiout.send_message(
            [0x90, message.note + noteShift, message.velocity])
    if(message.type == 'note_off'):

        midiout.send_message(
            [0x80, message.note + noteShift, message.velocity])

del midiout
