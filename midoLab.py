from mido import MidiFile
import mido
mid = MidiFile('midi.mid')
port = mido.open_output()

for msg in mid.play():
    print(mid)
    port.send(msg)
