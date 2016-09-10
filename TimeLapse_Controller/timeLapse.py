#!/usr/bin/python

from time import gmtime, strftime

import time
import os

on = True

while (on):
        x = str(strftime("%H:%M:%S"))
        m = int(strftime("%M"))
        if (m % 5 == 0):
                os.system("fswebcam --no-banner --set brightness=10% " + x + ".jpg")
                time.sleep(60)
                os.system("sudo reboot")
