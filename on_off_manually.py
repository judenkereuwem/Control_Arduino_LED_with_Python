#Python program to turn ON/OFF Arduino LED
#Jude Nkereuwm
#24/06/21

import serial
import time

print("A program to ON/OFF your LED")
print("\nCommand Options: ")
print("type H to turn ON LED")
print("type L to turn OFF LED")
print("type Q to quit program")

ser = serial.Serial('COM4', 9600, timeout=1)
time.sleep(2)

user_input = 'L'
while user_input != 'q':
    user_input = input('\nEnter command : ')
    byte_command = str.encode(user_input)
    ser.write(byte_command)
    time.sleep(0.5)

print('q entered. Exiting the program')
ser.close()
