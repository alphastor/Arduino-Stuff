import serial
from tkinter import *

ser = serial.Serial("COM5", baudrate=9600, timeout = 1)

def clear():
     ser.write(b'a')
     ser.write(b'b')
     ser.write(b'c')
     ser.write(b'd')
     ser.write(b'e')
     ser.write(b'f')
     ser.write(b'g') 

     ser.write(b'h')
     ser.write(b'i')
     ser.write(b'j')
     ser.write(b'k')
     ser.write(b'l')
     ser.write(b'm')
     ser.write(b'n')   

def zero():
     ser.write(b'A')
     ser.write(b'B')
     ser.write(b'C')
     ser.write(b'D')
     ser.write(b'E')
     ser.write(b'F')
     ser.write(b'g')

def one():
     ser.write(b'a')
     ser.write(b'B')
     ser.write(b'C')
     ser.write(b'd')
     ser.write(b'e')
     ser.write(b'f')
     ser.write(b'g')

def two():
     ser.write(b'A')
     ser.write(b'B')
     ser.write(b'c')
     ser.write(b'D')
     ser.write(b'E')
     ser.write(b'f')
     ser.write(b'G')

def three():
     ser.write(b'A')
     ser.write(b'B')
     ser.write(b'C')
     ser.write(b'D')
     ser.write(b'e')
     ser.write(b'f')
     ser.write(b'G')

def four():
     ser.write(b'a')
     ser.write(b'B')
     ser.write(b'C')
     ser.write(b'd')
     ser.write(b'e')
     ser.write(b'F')
     ser.write(b'G')

def five():
     ser.write(b'A')
     ser.write(b'b')
     ser.write(b'C')
     ser.write(b'D')
     ser.write(b'e')
     ser.write(b'F')
     ser.write(b'G')

def six():
     ser.write(b'A')
     ser.write(b'b')
     ser.write(b'C')
     ser.write(b'D')
     ser.write(b'E')
     ser.write(b'F')
     ser.write(b'G')

def seven():
     ser.write(b'A')
     ser.write(b'B')
     ser.write(b'C')
     ser.write(b'd')
     ser.write(b'e')
     ser.write(b'f')
     ser.write(b'g')
     
def eight():
     ser.write(b'A')
     ser.write(b'B')
     ser.write(b'C')
     ser.write(b'D')
     ser.write(b'E')
     ser.write(b'F')
     ser.write(b'G')

def nine():
     ser.write(b'A')
     ser.write(b'B')
     ser.write(b'C')
     ser.write(b'D')
     ser.write(b'e')
     ser.write(b'F')
     ser.write(b'G')
#---------------------------------------------------------------------------------------------------------------#
funcs = {0: zero, 1: one, 2: two, 3: three, 4: four, 5: five, 6: six, 7: seven, 8: eight, 9: nine}  
keys = [0,1,2,3,4,5,6,7,8,9]

# creating tkinter window 
# win=TK() to win.mainloop() is the code for the elements of the window  
win = Tk() # body open
win.title("7_Seg_Ans_Displayer")

def calculate():
    if "+" in usr_val.get():
        a = usr_val.get().partition("+") # separate the user val for ex: usr_input = 2+2 output = ('2', '+', '2')
        b = int(a[0]) + int(a[2]) # convert the str to int and perform the calculation
        funcs[keys[b]]() # find the desired number from the def functions 

    elif "-" in usr_val.get():
        a = usr_val.get().partition("-")
        b = int(a[0]) - int(a[2])
        funcs[keys[b]]()

    elif "*" in usr_val.get():
        a = usr_val.get().partition("*")
        b = int(a[0]) * int(a[2])
        funcs[keys[b]]()

    elif "/" in usr_val.get():
        a = usr_val.get().partition("/")
        b = int(a[0]) / int(a[2])
        funcs[keys[b]]()

    else:
        print("No")
#---------------------------------------------------------------------------------------------------------------#
btn_calculate =  Button(win, text = "Calculate", width = 10, command=calculate) 
btn_clear = Button(win, text = "Clear", width = 10, command=clear)

# a varialbe to store user input as str value
usr_val = StringVar()
# initialising user input area
usr_input = Entry(win, textvariable = usr_val) 

# mapping the button and input box on the window 
usr_input.grid(row=0, column=0)
btn_clear.grid(row=0, column=1)
btn_calculate.grid(row=1, columnspan=2, sticky="ew")
#---------------------------------------------------------------------------------------------------------------#
win.mainloop() # body close    