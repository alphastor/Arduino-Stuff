from serial import *
from time import *
ser = Serial('COM6', baudrate=9600, timeout=1)

# def char_A():
#     ser.write(b'a')

# def char_B():
#     ser.write(b'b')
def char_A():
    ser.write(b'a')

def char_B():
    ser.write(b'b')

def char_C():
    ser.write(b'c')

def char_D():
    ser.write(b'd')

def char_E():
    ser.write(b'e')

def char_F():
    ser.write(b'f')