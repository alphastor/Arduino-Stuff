import serial
from tkinter import *














# creating tkinter window 
win = Tk()
win.title("7 Segment controller")

b_c = Button(win,text = "clear", width=10)
b_c.grid(row = 0, columnspan = 4, sticky = "ew")

b_1 = Button(win,text = "1", width=10)
b_1.grid(row = 1, column = 0)

b_2 = Button(win,text = "2", width=10)
b_2.grid(row = 1, column = 1)

b_3 = Button(win,text = "3", width=10)
b_3.grid(row = 1, column = 2)

b_p = Button(win, text = "+", width = 10)
b_p.grid(row = 1, column =  3)

#---------------------------------------------------------------------------------#

b_4 = Button(win,text = "4", width=10)
b_4.grid(row = 2, column = 0)

b_5 = Button(win,text = "5", width=10)
b_5.grid(row = 2, column = 1)

b_6 = Button(win,text = "6", width=10)
b_6.grid(row = 2, column = 2)

b_p = Button(win, text = "-", width = 10)
b_p.grid(row = 2, column =  3)

#---------------------------------------------------------------------------------#

b_7 = Button(win,text = "7", width=10)
b_7.grid(row = 3, column = 0)

b_8 = Button(win,text = "8", width=10)
b_8.grid(row = 3, column = 1)

b_9 = Button(win,text = "9", width=10)
b_9.grid(row = 3, column = 2)

b_p = Button(win, text = "*", width = 10)
b_p.grid(row = 3, column =  3)

#---------------------------------------------------------------------------------#

b_0 = Button(win,text = "0", width=10)
b_0.grid(row = 4, columnspan = 3, sticky = "ew")

b_p = Button(win, text = "/", width = 10)
b_p.grid(row = 4, column =  3)

#---------------------------------------------------------------------------------#

b_snake = Button(win,text = "Snake", width=10)
b_snake.grid(row = 5, columnspan = 3, sticky = "ew")

# if input ==2 prints 2 on 7 seg display
b_display = Button(win, text = "Display", width=10)
b_display.grid(row = 5, column = 3)

#---------------------------------------------------------------------------------#

user_val = StringVar()
usr_input = Entry(win, textvariable=user_val) 
usr_input.grid(row = 6, columnspan=4, sticky="ew")



#---------------------------------------------------------------------------------#

win.mainloop()
