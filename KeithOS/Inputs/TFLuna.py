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
        self.rawSpeed = 0
        self.ser = serial.Serial("/dev/serial0", 115200, timeout=0)
        self.set_samp_rate() 
        self.last10Points = []
        self.runTF()
    #
    ############################
    # read ToF data from TF-Luna
    ############################
    #
    def set_samp_rate(self,samp_rate=100):
        ##########################
    # change the sample rate
        samp_rate_packet = [0x5a,0x06,0x03,samp_rate,00,00] # sample rate byte array
        self.ser.write(samp_rate_packet) # send sample rate instruction
        time.sleep(0.1) # wait for change to take effect
        return
    currentDist = 0

    def SendNote(self, speed):
        print('Send note function not in use ')

    def read_tfluna_data(self):
        while True:
           # print('In dist loop 3')
            counter = self.ser.in_waiting  # count the number of bytes of the serial port
            #print('Counter ', str(counter ) )
            if counter > 8:
                bytes_serial = self.ser.read(9)  # read 9 bytes
                print(bytes_serial)
                self.ser.reset_input_buffer()  # reset buffer

                if bytes_serial[0] == 0x59 and bytes_serial[1] == 0x59:  # check first two bytes
                    print(bytes_serial)
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
            print('In dist loop ')
            try:
                if self.ser.isOpen() == False:
                    print('Ser OPEN ')
                    self.ser.open()  # open serial port if not open

            except Exception as id:
                print(id)
                
            print('In dist loop 2 ')
            try:
                distance, strength, temperature = self.read_tfluna_data()  # read values
                print( 'Loc distance' , distance)
                self.currentDist = distance
                if distance > 100:
                    continue

                self.last10Points.append(distance)
                if len(self.last10Points) > 9:
                    absSpeed = abs(max(self.last10Points) -
                                   min(self.last10Points))
                    speed = absSpeed / .1
                    print(self.last10Points, ":", absSpeed)

                    self.rawSpeed = speed
                    self.last10Points.clear()
                    if(speed > 60):
                        self.SendNote(speed)
                        time.sleep(0.1)

                        # self.speed = 0
                # print("Dist CM :" + str(self.currentDist))

                self.currentTemp = temperature
                self.currentStrength = strength
                # print('Distance: {0:2.2f} cm, Strength: {1:2.0f} / 65535 (16-bit), Chip Temperature: {2:2.1f} C'.
                #      format(distance, strength, temperature))  # print sample data
            except Exception as id:
                print(str(id))
            time.sleep(.01)

    def runTF(self):
        tfThread = threading.Thread(target=self.StartDistLoop)
        tfThread.start()
