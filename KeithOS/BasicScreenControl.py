# https://github.com/adafruit/Adafruit_Python_SSD1306
import threading
import subprocess
import time

import Adafruit_GPIO.SPI as SPI
import Adafruit_SSD1306
import os
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont


# https://www.raspberrypi-spy.co.uk/2018/04/i2c-oled-display-module-with-raspberry-pi/


class BasicScreenControl:

    # Can render about 13 letters safely per line
    # 4 lines
    currentTexts = ["Awaiting Input "]
    shutDown = False

# Raspberry Pi pin configuration:
    RST = None     # on the PiOLED this pin isnt used
# Note the following are only used with SPI:
    DC = 23
    SPI_PORT = 0
    SPI_DEVICE = 0
    fontSize = 15
    disp = Adafruit_SSD1306.SSD1306_128_64(rst=RST)

    def __init__(self):
        self.disp.begin()

        self.disp.clear()
        self.disp.display()

        self.width = self.disp.width
        self.height = self.disp.height
        self.image = Image.new('1', (self.width, self.height))

        self.draw = ImageDraw.Draw(self.image)

        self.draw.rectangle(
            (0, 0, self. width, self.height), outline=0, fill=0)

        self.padding = -2
        self.top = self.padding
        self.bottom = self.height-self.padding
        self.x = 0

        dn = os.path.dirname(os.path.realpath(__file__))

        #midiPath = os.path.join(dn, 'fonts', 'BodoniXT.ttf')

        #self.font = ImageFont.truetype(midiPath, self.fontSize)
       # print(self.font)
        self.i = 0
        self.runScreen()
        time.sleep(3)
        self.updateText(self.getIP())
        time.sleep(3)

    def updateText(self, *texts):
        self.currentTexts = texts

    def getIP(self):
        cmd = "hostname -I | cut -d\' \' -f1"
        IP = subprocess.check_output(cmd, shell=True)
        return IP

    def runScreen(self):
        screenThread = threading.Thread(target=self.runScreenInternal)
        screenThread.start()

    def runScreenInternal(self):
        while True:

            if(self.shutDown):

                self.updateText("")
                self.drawnScreen()
                # self.disp.reset()
                break

            self.drawnScreen()

    def drawnScreen(self):
        self.i = self.i+1

        self.draw.rectangle((0, 0, self.width, self.height), outline=0, fill=0)

        cmd = "hostname -I | cut -d\' \' -f1"
        IP = subprocess.check_output(cmd, shell=True)
        cmd = "top -bn1 | grep load | awk '{printf \"CPU Load: %.2f\", $(NF-2)}'"
        CPU = subprocess.check_output(cmd, shell=True)
        cmd = "free -m | awk 'NR==2{printf \"Mem: %s/%sMB %.2f%%\", $3,$2,$3*100/$2 }'"
        MemUsage = subprocess.check_output(cmd, shell=True)
        cmd = "df -h | awk '$NF==\"/\"{printf \"Disk: %d/%dGB %s\", $3,$2,$5}'"
        Disk = subprocess.check_output(cmd, shell=True)
        #  font=self.font
        for index, newString in enumerate(self.currentTexts):
            self.draw.text((self.x, self.top + index * self.fontSize),       "" +
                           str(newString), fill=255)

        self.disp.image(self.image)
        self.disp.display()
        time.sleep(.01)

    def off(self):
        self.shutDown = True
