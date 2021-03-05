from mido import MidiFile
import mido
mid = MidiFile('midi.mid')
port = mido.open_output()

for msg in MidiFile('song.mid').play():
    port.send(msg)
