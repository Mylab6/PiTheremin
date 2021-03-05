from mido.ports import BaseOutput
from mido import MidiFile
import mido
mid = MidiFile('midi.mid')
port = PrintPort()

for msg in mid.play():
    print(msg)
    port.send(msg)


class PrintPort(BaseOutput):
    def _send(message):
        print(message.dict())
