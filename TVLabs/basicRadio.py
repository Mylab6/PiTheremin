import time
import os

os.system("echo 'as' | cec-client -s -d 1")
os.system("mplayer  http://130.166.82.14:8002")

time.sleep(60)
os.system("echo 'standby 0' | cec-client -s -d 1")
