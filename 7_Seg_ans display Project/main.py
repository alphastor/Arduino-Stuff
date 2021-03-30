from tkinter import *
from display1 import *

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