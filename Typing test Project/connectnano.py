from serial import *
from time import *
ser = Serial('COM6', baudrate=9600, timeout=1)

# def char_A():
#     ser.write(b'a')

# def char_B():
#     ser.write(b'b')
def char_A():
    ser.write(b'a')

def char_clear():
    ser.write(b'-')

# def char_b():
