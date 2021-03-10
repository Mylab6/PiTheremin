######################################################
# Copyright (c) 2021 Maker Portal LLC
# Author: Joshua Hrisko
######################################################
#
# TF-Luna Mini LiDAR wired to a Raspberry Pi via UART
# --- testing the distance measurement from the TF-Luna
#
#
######################################################
#
import serial
import time
import numpy as np

import threading


class TFLuna():

    #
    ##########################
    # TFLuna Lidar
    ##########################
    #
    # mini UART serial device
    def __init__(self):
        self.speed = 0
        self.ser = serial.Serial("/dev/serial0", 115200, timeout=0)
        self.last10Points = []
        self.runTF()
    #
    ############################
    # read ToF data from TF-Luna
    ############################
    #
    currentDist = 0

    def read_tfluna_data(self):
        while True:
            counter = self.ser.in_waiting  # count the number of bytes of the serial port
            if counter > 8:
                bytes_serial = self.ser.read(9)  # read 9 bytes
                self.ser.reset_input_buffer()  # reset buffer

                if bytes_serial[0] == 0x59 and bytes_serial[1] == 0x59:  # check first two bytes
                    # distance in next two bytes
                    distance = bytes_serial[2] + bytes_serial[3]*256
                    # signal strength in next two bytes
                    strength = bytes_serial[4] + bytes_serial[5]*256
                    # temp in next two bytes
                    temperature = bytes_serial[6] + bytes_serial[7]*256
                    temperature = (temperature/8.0) - \
                        256.0  # temp scaling and offset
                    return distance,  strength, temperature

    def StartDistLoop(self):
        while True:
            if self.ser.isOpen() == False:
                self.ser.open()  # open serial port if not open

            try:
                distance, strength, temperature = self.read_tfluna_data()  # read values
                # print(distance)
                self.currentDist = distance
                if len(self.last10Points) > 9:
                    self.speed = max(self.last10Points) - \
                        min(self.last10Points) / .1
                    self.last10Points.clear()

                self.last10Points.append(distance)
                self.currentTemp = temperature
                self.currentStrength = strength
                # print('Distance: {0:2.2f} cm, Strength: {1:2.0f} / 65535 (16-bit), Chip Temperature: {2:2.1f} C'.
                #      format(distance, strength, temperature))  # print sample data
            except Exception as id:
                print(str(id))
            time.sleep(.01)
            if(self.speed > 60):
                self.SendNote(self.speed)
                time.sleep(0.2)

                self.speed = 0

    def runTF(self):
        tfThread = threading.Thread(target=self.StartDistLoop)
        tfThread.start()
