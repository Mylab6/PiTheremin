
import subprocess
import time

import Adafruit_GPIO.SPI as SPI
import Adafruit_SSD1306
import os
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
from gpiozero import Button


class ScreenLabs:
    button = Button(4)


# Raspberry Pi pin configuration:
    RST = None     # on the PiOLED this pin isnt used
# Note the following are only used with SPI:
    DC = 23
    SPI_PORT = 0
    SPI_DEVICE = 0

# Beaglebone Black pin configuration:
# RST = 'P9_12'
# Note the following are only used with SPI:
# DC = 'P9_15'
# SPI_PORT = 1
# SPI_DEVICE = 0

# 128x32 display with hardware I2C:
#disp = Adafruit_SSD1306.SSD1306_128_32(rst=RST)

# 128x64 display with hardware I2C:
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
        self.font = ImageFont.truetype(midiPath, 16)
        print(self.font)
        self.i = 0

    def updateScreen(self):
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

        self.draw.text((self.x, self.top),       "" +
                       str(self.i),  font=self.font, fill=255)

        self.disp.image(self.image)
        self.disp.display()
        time.sleep(.01)


screen = ScreenLabs()
while True:
    screen.updateScreen()
