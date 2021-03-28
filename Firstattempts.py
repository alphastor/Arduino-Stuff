'''pyfirmata is module to control arduino:- uno,nano,mega,etc, 
this is a simple blink tst pin 13 is where the onboard led is connected to'''
import pyfirmata as pf
import time as t 
pin = 13
port = "COM5"
board = pf.Arduino(port)
for i in range(10):
    board.digital[pin].write(1)
    print("on")
    t.sleep(1)
    board.digital[pin].write(0)
    print("off")
    t.sleep(1)