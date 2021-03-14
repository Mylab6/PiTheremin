from rtmidi.midiutil import open_midioutput
from rtmidi.midiutil import open_midiinput


class BasicControllableItem:
    def __init__(self, screenInstance, buttonInstance, rotaryReadInstance, tfInstance):
        self.screen = screenInstance
        self.button = buttonInstance
        self.rotaryReadInstance = rotaryReadInstance
        self.tfReader = tfInstance

        # self.rotaryReadInstance.runDial()


class BasicMidiIn:

    def __init__(self, midiPort=1):
        self.midiInput, self.port_name = open_midiinput(midiPort)

    def checkForMidiMssg(self):
        msg = self.midiInput.get_message()


class ControllableMidiItem(BasicControllableItem):

    def __init__(self, screen, button19,
                 rotaryReadInstance, tfInstance, midiout ):
        self.midiout = midiout

        super().__init__(screen, button19,
                         rotaryReadInstance, tfInstance)

    def sendMidi(self, note, velocity, command):

        self.midiout.send_message(
            [command, note, velocity])

    def sendNoteOn(self, note, velocity=112):
        print('Send MIDI ',  velocity,  note)
        self.sendMidi(note, velocity, 0x90)

    def sendNoteOff(self, note, velocity=112):
        self.sendMidi(note, velocity, 0x80)
