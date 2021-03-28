'''pyfirmata is module to control arduino:- uno,nano,mega,etc, 
this is a simple blink tst pin 13 is where the onboard led is connected to'''
# import pyfirmata as pf
# import time as t 
# pin = 13
# port = "COM5"
# board = pf.Arduino(port)
# for i in range(10):
#     board.digital[pin].write(1)
#     print("on")
#     t.sleep(1)
#     board.digital[pin].write(0)
#     print("off")
#     t.sleep(1)

'''takes a input for for file name and blinks led onboard for the same 
and then takes info for the file and the after printing ot to the file 
blinks the led thrice for the same'''
# import pyfirmata as pyf
# import time as t
# import sys

# pin = 13
# board = pyf.Arduino("COM5")

# f_nm = input("Enter file name (with extension): ")
# board.digital[pin].write(1)
# t.sleep(0.2)
# board.digital[pin].write(0)
# t.sleep(0.2)

# print("Enter txt to store in the file:- \n\t\t")
# f = open(f_nm,"r+")
# info = sys.stdin.read()

# prt = f.write(info)
# for i in range(3):
#     board.digital[pin].write(1)
#     t.sleep(0.2)
#     board.digital[pin].write(0)
#     t.sleep(0.2)

# f.close()
