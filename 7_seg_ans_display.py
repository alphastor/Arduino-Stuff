import serial
from tkinter import *
import tkinter as tk 
#--------------------------------------------------------------------#

#making connection with Arduino
ser = serial.Serial('COM5', baudrate = 9600, timeout = 1) 

#--------------------------------------------------------------------#

def turnOnLED():
    ser.write(b'a')

def turnOffLED(): 
    ser.write(b'!')

#--------------------------------------------------------------------#
# creating tkinter window 
root = Tk() 
root.title('Blink GUI')

btn_On= tk.Button(root, text="Turn On", command=turnOnLED)
btn_On.grid(row=0, column=0)

btn_Off = tk.Button(root, text="Turn Off", command=turnOffLED)
btn_Off.grid(row=0, column=1)

root.geometry("350x350")
root.mainloop()

#--------------------------------------------------------------------#