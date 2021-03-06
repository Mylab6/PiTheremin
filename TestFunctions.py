import time

from BasicScreenControl import BasicScreenControl
screen = BasicScreenControl()
screen.runScreen()
i = 0
while True:
    i = i + 1
    screen.updateText("Dream", str(i))
    time.sleep(.01)
