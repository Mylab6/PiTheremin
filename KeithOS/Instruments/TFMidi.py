
from KeithOS.Instruments.BasicControllableItem import ControllableMidiItem
import time
import os 
import sys

# https://www.mutopiaproject.org/cgibin/make-table.cgi?collection=bachis&preview=1


class TFMidi(ControllableMidiItem):
    lastNote = False
    orignalNote = 58
    noteSpeed = 0
    @property
    def baseNote(self):
        return self.orignalNote + self.rotaryReadInstance.rotateValue

    def __init__(self, screen, button19,
                 rotaryReadInstance, tfInstance, midiout ) :
        # self.legacySetUp()
        # self.IP = self.getIP()
        
        tfInstance.SendNote = self.SendNote

        super().__init__(screen, button19,
                         rotaryReadInstance, tfInstance, midiout)


    def createTextArr(self):
         self.textArr =  ["Current Note " +
                    str(self.lastNote),  "Note Speed: " +
                    str(self.noteSpeed), 'Base Note :' + str(self.baseNote),
                    self.screen.getIP()]


    def SendNote(self, speed):
        
        self.noteSpeed = speed
       # self.MidiInClass.checkForMidiMssg()

        if(self.lastNote):
            self.sendNoteOff(self.lastNote)

        # time.sleep(.31)
        self.lastNote = min(
            75,  self.baseNote + self.tfReader.currentDist / 4)

        if(speed > 60):
            self.sendNoteOn(
                self.lastNote)

        # time.sleep(1)

# TestMidi().runScreen()

"""     def legacySetUp(self):
        self.screen = BasicScreenControl()

        self.MidiInClass = BasicMidiIn()
        self.rotaryReadInstance = RotaryRead()
        self.rotaryReadInstance.runDial()
        self.tfReader = TFLuna()
        self.tfReader.SendNote = self.SendNote
        self.button = Button(19) """
