from mido.ports import BaseOutput
from mido import MidiFile
import mido


class PrintPort(BaseOutput):
    def _send(self, message):
        print(message.dict())


mid = MidiFile('midi.mid')
port = PrintPort()

for msg in mid.play():
    print(msg)
    port.send(msg)
