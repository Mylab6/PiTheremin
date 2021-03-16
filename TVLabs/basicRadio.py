import time
import os

os.system("echo 'as' | cec-client -s -d 1")
os.system("mplayer  http://bbcmedia.ic.llnwd.net/stream/bbcmedia_radio1_mf_p")

time.sleep(60)
os.system("echo 'standby 0' | cec-client -s -d 1")
