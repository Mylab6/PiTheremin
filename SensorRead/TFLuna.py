######################################################
# Copyright (c) 2021 Maker Portal LLC
# Author: Joshua Hrisko
######################################################
#
# TF-Luna Mini LiDAR wired to a Raspberry Pi via UART
# --- Configuring the TF-Luna's baudrate, sample rate,
# --- and printing out the device version info
#
#
######################################################
#
import serial
import time
import numpy as np
#
############################
# Serial Functions
############################
#

# mini UART serial device
ser = serial.Serial("/dev/serial0", 115200, timeout=0)

print(ser)
if ser.isOpen() == False:
    ser.open()
    print(ser)
