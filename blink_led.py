#Python program to turn blink Arduino LED
#Jude Nkereuwm
#24/06/21

import serial
import time

ser = serial.Serial('COM4', 9600, timeout=1)
time.sleep(2)

for i in range(10):
    ser.write(b'H')
    time.sleep(0.5)
    ser.write(b'L')
    time.sleep(0.5)

ser.close()
