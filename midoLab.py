from mido.ports import BaseOutput
from mido import MidiFile
from rtmidi.midiutil import open_midioutput

import mido


mid = MidiFile('midi.mid')
#port = PrintPort()
midiout, port_name = open_midioutput(1)
for message in mid.play():
    # print(msg)
    # port.send(msg)
    if(message.type == 'note_on'):
        print('send note ON ')
        midiout.send_message([0x90, message.note, message.velocity])
    if(message.type == 'note_off'):

        midiout.send_message([0x80, message.note, message.velocity])
