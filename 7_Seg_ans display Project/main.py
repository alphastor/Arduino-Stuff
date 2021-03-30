from tkinter import *
from display1 import *

#---------------------------------------------------------------------------------------------------------------#

funcs_1 = {'0': zero, '1': one, '2': two, '3': three, '4': four, '5': five, '6': six, '7': seven, '8': eight, '9': nine}  
keys = ['0','1','2','3','4','5','6','7','8','9']

funcs_2 = {'0_2': zero_2, '1_2': one_2, '2_2': two_2, '3_2': three_2, '4_2': four_2, '5_2': five_2, '6_2': six_2, '7_2': seven_2, '8_2': eight_2, '9_2': nine_2}
keyz = ['0_2', '1_2', '2_2', '3_2', '4_2', '5_2', '6_2', '7_2', '8_2', '9_2']

# creating tkinter window, win=TK() to win.mainloop() is the code for the elements of the window
win = Tk() # body open
win.title("7_Seg_Ans_Displayer")

def calculate():
    if "+" in usr_val.get():
        a = usr_val.get().partition("+") # separate the user val for ex: usr_input = 2+2 output = ('2', '+', '2')
        b = int(a[0]) + int(a[2]) # convert the str to int and perform the calculation
        c = str(b) # converting b to str and store to c

        if len(c)==2:
            num_1 = int(c[0])
            num_2 = int(c[1])
            # print(num_1,num_2)
            funcs_1[keys[num_1]]()
            funcs_2[keyz[num_2]]() # for ex: if c[1] == "3" then c[1]+"_2" = "3_2" 
        elif len(c)==1:
            funcs_1[keys[0]]()
            funcs_2[keyz[b]]() # find the desired number from the def functions 
            
    elif "-" in usr_val.get():
        a = usr_val.get().partition("-")
        b = int(a[0]) - int(a[2])
        c = str(b) # converting b to str and store to c

        if len(c)==2:
            num_1 = int(c[0])
            num_2 = int(c[1])
            # print(num_1,num_2)
            funcs_1[keys[num_1]]()
            funcs_2[keyz[num_2]]() # for ex: if c[1] == "3" then c[1]+"_2" = "3_2" 
        elif len(c)==1:
            funcs_1[keys[0]]()
            funcs_2[keyz[b]]() # find the desired number from the def functions 

    elif "*" in usr_val.get():
        a = usr_val.get().partition("*")
        b = int(a[0]) * int(a[2])
        c = str(b) # converting b to str and store to c

        if len(c)==2:
            num_1 = int(c[0])
            num_2 = int(c[1])
            # print(num_1,num_2)
            funcs_1[keys[num_1]]()
            funcs_2[keyz[num_2]]() # for ex: if c[1] == "3" then c[1]+"_2" = "3_2" 
        elif len(c)==1:
            funcs_1[keys[0]]()
            funcs_2[keyz[b]]() # find the desired number from the def functions 

    elif "/" in usr_val.get():
        a = usr_val.get().partition("/")
        b = int(a[0]) // int(a[2])
        c = str(b) # converting b to str and store to c

        if len(c)==2:
            num_1 = int(c[0])
            num_2 = int(c[1])
            # print(num_1,num_2)
            funcs_1[keys[num_1]]()
            funcs_2[keyz[num_2]]() # for ex: if c[1] == "3" then c[1]+"_2" = "3_2" 
        elif len(c)==1:
            funcs_1[keys[0]]()
            funcs_2[keyz[b]]() # find the desired number from the def functions 

    else:
        print("No")

#---------------------------------------------------------------------------------------------------------------#

btn_calculate =  Button(win, text = "Calculate", width = 10, command=calculate) 
btn_cleardisplay = Button(win, text = "Clear Display", width = 10, command=clear)
btn_clear = Button(win, text = "Clear", width = 10)

usr_val = StringVar() # a varialbe to store user input as str type
usr_input = Entry(win, textvariable = usr_val) # initialising user input area

# mapping the button and input box on the window 
usr_input.grid(row=0, column=0)
btn_clear.grid(row=0, column=1)
btn_calculate.grid(row=1, column=0, sticky="ew")
btn_cleardisplay.grid(row=1, column=1)

#---------------------------------------------------------------------------------------------------------------#
win.mainloop() # body close    