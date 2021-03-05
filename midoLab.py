from mido.ports import BaseOutput
from mido import MidiFile
from rtmidi.midiutil import open_midioutput

import mido


class PrintPort(BaseOutput):
    def _send(self, message):
        # print(message.dict())
        if(message.type == 'note_on'):
            print('send note ON ')
            self.midiout.send_message([0x90, message.note, message.velocity])
        if(message.type == 'note_off'):

            self.midiout.send_message([0x80, message.note, message.velocity])

    def __open(self, **kwargs):
        midiout, port_name = open_midioutput(1)
        self.midiout = midiout


mid = MidiFile('midi.mid')
port = PrintPort()

for msg in mid.play():
    # print(msg)
    port.send(msg)
