from rtmidi.midiutil import open_midioutput
from rtmidi.midiutil import open_midiinput
import threading
import time
import os 


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
    def runScreen(self):
        self.textArr = "Waiting For implimentation"
        
        self.screenThread = threading.Thread(target=self.updateScreen)
        self.screenThread.start()
    def createTextArr(self):
        self.textArr = "No Implimentation"

    def updateScreen(self):
       
        exitInt = 0 
        while True:
            self.createTextArr()     
            time.sleep(.35)

            if self.button.is_pressed:
                exitInt = exitInt + 1 
                self.screen.updateText("Hold For Exit" , str(exitInt) )
                if(exitInt > 10):
                   
                   
                    self.screen.updateText("Exiting ?" )
                    os.system('sudo reboot')

                    
            else:

                if( exitInt > 1):
                     exitInt = exitInt -1 
                self.screen.updateText(
                  *self.textArr
                )



