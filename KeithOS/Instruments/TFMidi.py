
from KeithOS.Instruments.BasicControllableItem import ControllableMidiItem
import time
import threading
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
                 rotaryReadInstance, tfInstance, midiout, killCommand ) :
        # self.legacySetUp()
        # self.IP = self.getIP()
        self.killCommand = killCommand
        tfInstance.SendNote = self.SendNote

        super().__init__(screen, button19,
                         rotaryReadInstance, tfInstance, midiout)

    def updateScreen(self):
        exitInt = 0 
        while self.runMe:
            
            time.sleep(.35)

            if self.button.is_pressed:
                exitInt = exitInt + 1 
                self.screen.updateText("Hold For Exit" , str(exitInt) )
                if(exitInt > 10):
                    self.runMe = False
                   
                    self.screen.updateText("Exiting ?" )
                    os.system('sudo reboot')

                    
            else:

                if( exitInt > 1):
                     exitInt = exitInt -1 
                self.screen.updateText(

                    "Current Note " +
                    str(self.lastNote),  "Note Speed: " +
                    str(self.noteSpeed), 'Base Note :' + str(self.baseNote),
                    self.screen.getIP()
                )

        # while True:
        #    self.SendNote()

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
    def runScreen(self):
        self.runMe = True 
        self.screenThread = threading.Thread(target=self.updateScreen)
        self.screenThread.start()


# TestMidi().runScreen()

"""     def legacySetUp(self):
        self.screen = BasicScreenControl()

        self.MidiInClass = BasicMidiIn()
        self.rotaryReadInstance = RotaryRead()
        self.rotaryReadInstance.runDial()
        self.tfReader = TFLuna()
        self.tfReader.SendNote = self.SendNote
        self.button = Button(19) """
