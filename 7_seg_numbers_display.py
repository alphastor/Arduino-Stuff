# a = 2
# b = 3
# c = 4
# d = 5
# e = 6
# f = 7
# g = 8

# a_2 = 9
# b_2 = 10
# c_2 = 11
# d_2 = 12
# e_2 = 13
# f_2 = A0
# g_2 = A1

#--------------------------------------------------------------------#

import serial
from tkinter import *
import time as t

#--------------------------------------------------------------------#

#making connection with Arduino
ser = serial.Serial('COM5', baudrate = 9600, timeout = 1) 

#--------------------------------------------------------------------#

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

def snake():
     for i in range(5):
        ser.write(b'A')
        t.sleep(0.1)
        ser.write(b'a')
        ser.write(b'H')

        t.sleep(0.1)
        ser.write(b'h')
        ser.write(b'I')

        t.sleep(0.1)
        ser.write(b'i')
        ser.write(b'N')

        t.sleep(0.1)
        ser.write(b'n')
        ser.write(b'G')

        t.sleep(0.1)
        ser.write(b'g')
        ser.write(b'E')

        t.sleep(0.1)
        ser.write(b'e')
        ser.write(b'D')

        t.sleep(0.1)
        ser.write(b'd')
        ser.write(b'K')

        t.sleep(0.1)
        ser.write(b'k')
        ser.write(b'J')

        t.sleep(0.1)
        ser.write(b'j')
        ser.write(b'N')

        t.sleep(0.1)
        ser.write(b'n')
        ser.write(b'G')

        t.sleep(0.1)
        ser.write(b'g')
        ser.write(b'F')

        t.sleep(0.1)
        ser.write(b'f')

def display():
     if user_val.get() == "2":
          two()


#--------------------------------------------------------------------#

# creating tkinter window 
win = Tk()
win.title("7 Segment controller")

b_c = Button(win,text = "clear", width=10, command = clear)
b_c.grid(row = 0, columnspan = 4, sticky = "ew")

b_1 = Button(win,text = "1", width=10, command = one)
b_1.grid(row = 1, column = 0)

b_2 = Button(win,text = "2", width=10, command = two)
b_2.grid(row = 1, column = 1)

b_3 = Button(win,text = "3", width=10, command = three)
b_3.grid(row = 1, column = 2)

b_p = Button(win, text = "+", width = 10)
b_p.grid(row = 1, column =  3)

#---------------------------------------------------------------------------------#

b_4 = Button(win,text = "4", width=10, command = four)
b_4.grid(row = 2, column = 0)

b_5 = Button(win,text = "5", width=10, command = five)
b_5.grid(row = 2, column = 1)

b_6 = Button(win,text = "6", width=10, command = six)
b_6.grid(row = 2, column = 2)

b_p = Button(win, text = "-", width = 10)
b_p.grid(row = 2, column =  3)

#---------------------------------------------------------------------------------#

b_7 = Button(win,text = "7", width=10, command = seven)
b_7.grid(row = 3, column = 0)

b_8 = Button(win,text = "8", width=10, command = eight)
b_8.grid(row = 3, column = 1)

b_9 = Button(win,text = "9", width=10, command = nine)
b_9.grid(row = 3, column = 2)

b_p = Button(win, text = "*", width = 10)
b_p.grid(row = 3, column =  3)

#---------------------------------------------------------------------------------#

b_0 = Button(win,text = "0", width=10, command = zero)
b_0.grid(row = 4, columnspan = 3, sticky = "ew")

b_p = Button(win, text = "/", width = 10)
b_p.grid(row = 4, column =  3)

#---------------------------------------------------------------------------------#

b_snake = Button(win,text = "Snake", width=10, command = snake)
b_snake.grid(row = 5, columnspan = 3, sticky = "ew")

# if input ==2 prints 2 on 7 seg display
b_display = Button(win, text = "Display", width=10, command = display)
b_display.grid(row = 5, column = 3)

#---------------------------------------------------------------------------------#

user_val = StringVar()
usr_input = Entry(win, textvariable=user_val) 
usr_input.grid(row = 6, columnspan=4, sticky="ew")



#---------------------------------------------------------------------------------#

win.mainloop()

#--------------------------------------------------------------------#