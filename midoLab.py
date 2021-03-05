from mido import MidiFile, port

mid = MidiFile('midi.mid')

for msg in MidiFile('song.mid').play():
    port.send(msg)
