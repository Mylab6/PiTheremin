
import subprocess
import time

import Adafruit_GPIO.SPI as SPI
import Adafruit_SSD1306
import os
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
from gpiozero import Button
import threading


class ScreenLabs:
    button = Button(4)
    # Can render about 13 letters safely per line
    # 4 lines
    currentTexts = ["hat", "cat", "dog",
                    '123456789ABCDEFG', '390290620923451']

# Raspberry Pi pin configuration:
    RST = None     # on the PiOLED this pin isnt used
# Note the following are only used with SPI:
    DC = 23
    SPI_PORT = 0
    SPI_DEVICE = 0
    fontSize = 16
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

        midiPath = os.path.join(dn, 'fonts', 'BodoniXT.ttf')

        self.font = ImageFont.truetype(midiPath, self.fontSize)
       # print(self.font)
        self.i = 0
        # self.runScreen()

    def updateText(self, *texts):
        self.currentTexts = texts

    def runScreen(self):
        screenThread = threading.Thread(target=self.runScreenInternal)
        screenThread.start()

    def runScreenInternal(self):
        while True:
            self.updateScreen()

    def updateScreen(self):
        print('Update screen')
        self.i = self.i+1

        if self.button.is_pressed:
            print("Button is pressed")
        self.draw.rectangle((0, 0, self.width, self.height), outline=0, fill=0)

        cmd = "hostname -I | cut -d\' \' -f1"
        IP = subprocess.check_output(cmd, shell=True)
        cmd = "top -bn1 | grep load | awk '{printf \"CPU Load: %.2f\", $(NF-2)}'"
        CPU = subprocess.check_output(cmd, shell=True)
        cmd = "free -m | awk 'NR==2{printf \"Mem: %s/%sMB %.2f%%\", $3,$2,$3*100/$2 }'"
        MemUsage = subprocess.check_output(cmd, shell=True)
        cmd = "df -h | awk '$NF==\"/\"{printf \"Disk: %d/%dGB %s\", $3,$2,$5}'"
        Disk = subprocess.check_output(cmd, shell=True)
# for count, value in enumerate(values):
        # screenSpacing = 16
        for index, newString in enumerate(self.currentTexts):
            self.draw.text((self.x, self.top + index * self.fontSize),       "" +
                           str(newString),  font=self.font, fill=255)

        self.disp.image(self.image)
        self.disp.display()
        time.sleep(.01)


screen = ScreenLabs()
screen.runScreen()
i = 0
while True:
    i = i + 1
    screen.updateText("Dream", str(i))
    time.sleep(.01)
