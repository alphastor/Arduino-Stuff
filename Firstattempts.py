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

'''controls a external led'''
# import pyfirmata as pf
# import time as t
# board = pf.Arduino("COM5")
# for i in range(20):
#     board.digital[6].write(1)
#     print("on")
#     t.sleep(0.1)
#     board.digital[6].write(0)
#     print("off")
#     t.sleep(0.1)

'''controlling led through buttons using tkinter'''
# import pyfirmata as pf
# from tkinter import *
# board = pf.Arduino("COM5")
# def on():
#     board.digital[6].write(1)
#     print("On")
# def off():
#     board.digital[6].write(0)
#     print("Off")
# win = Tk()
# win.title("Led controller")
# b_1 = Button(win,text = "On", command=on, width=10)
# b_1.grid(row = 0, column = 0, padx=50)
# b_2 = Button(win,text = "Off", command=off, width=10)
# b_2.grid(row = 1, column = 0, padx=50)
# win.mainloop()

'''working with 7 segment displaying numbers/characters, this code displays the number 7'''
# import pyfirmata as pf
# a = 3
# b = 2
# c = 8
# d = 7
# e = 6
# f = 4
# g = 5
# seg_7 = pf.Arduino("COM5")
# seg_7.digital[a].write(1)
# seg_7.digital[b].write(1)
# seg_7.digital[c].write(1)

'''Displays numbers on 7 seg on pressing the buttons'''
# import pyfirmata as pf
# from tkinter import *

# a = 3
# b = 2
# c = 8
# d = 7
# e = 6
# f = 4
# g = 5
# seg_7 = pf.Arduino("COM5")

# def zero():
#     seg_7.digital[a].write(1)
#     seg_7.digital[b].write(1)
#     seg_7.digital[c].write(1)
#     seg_7.digital[d].write(1)
#     seg_7.digital[e].write(1)
#     seg_7.digital[f].write(1)
#     seg_7.digital[g].write(0)

# def one():
#     seg_7.digital[a].write(0)
#     seg_7.digital[b].write(1)
#     seg_7.digital[c].write(1)
#     seg_7.digital[d].write(0)
#     seg_7.digital[e].write(0)
#     seg_7.digital[f].write(0)
#     seg_7.digital[g].write(0)

# def two():
#     seg_7.digital[a].write(1)
#     seg_7.digital[b].write(1)
#     seg_7.digital[c].write(0)
#     seg_7.digital[d].write(1)
#     seg_7.digital[e].write(1)
#     seg_7.digital[f].write(0)
#     seg_7.digital[g].write(1)

# def three():
#     seg_7.digital[a].write(1)
#     seg_7.digital[b].write(1)
#     seg_7.digital[c].write(1)
#     seg_7.digital[d].write(1)
#     seg_7.digital[e].write(0)
#     seg_7.digital[f].write(0)
#     seg_7.digital[g].write(1)

# def four():
#     seg_7.digital[a].write(0)
#     seg_7.digital[b].write(1)
#     seg_7.digital[c].write(1)
#     seg_7.digital[d].write(0)
#     seg_7.digital[e].write(0)
#     seg_7.digital[f].write(1)
#     seg_7.digital[g].write(1)

# def five():
#     seg_7.digital[a].write(1)
#     seg_7.digital[b].write(0)
#     seg_7.digital[c].write(1)
#     seg_7.digital[d].write(1)
#     seg_7.digital[e].write(0)
#     seg_7.digital[f].write(1)
#     seg_7.digital[g].write(1)

# def six():
#     seg_7.digital[a].write(1)
#     seg_7.digital[b].write(0)
#     seg_7.digital[c].write(1)
#     seg_7.digital[d].write(1)
#     seg_7.digital[e].write(1)
#     seg_7.digital[f].write(1)
#     seg_7.digital[g].write(1)

# def seven():
#     seg_7.digital[a].write(1)
#     seg_7.digital[b].write(1)
#     seg_7.digital[c].write(1)
#     seg_7.digital[d].write(0)
#     seg_7.digital[e].write(0)
#     seg_7.digital[f].write(0)
#     seg_7.digital[g].write(0)

# def eight():
#     seg_7.digital[a].write(1)
#     seg_7.digital[b].write(1)
#     seg_7.digital[c].write(1)
#     seg_7.digital[d].write(1)
#     seg_7.digital[e].write(1)
#     seg_7.digital[f].write(1)
#     seg_7.digital[g].write(1)

# def nine():
#     seg_7.digital[a].write(1)
#     seg_7.digital[b].write(1)
#     seg_7.digital[c].write(1)
#     seg_7.digital[d].write(1)
#     seg_7.digital[e].write(0)
#     seg_7.digital[f].write(1)
#     seg_7.digital[g].write(1)

# win = Tk()
# win.title("7 Segment controller")

# b_1 = Button(win,text = "1", width=10, command = one)
# b_1.grid(row = 0, column = 0)

# b_2 = Button(win,text = "2", width=10, command = two)
# b_2.grid(row = 0, column = 1)

# b_3 = Button(win,text = "3", width=10, command = three)
# b_3.grid(row = 0, column = 2)

# b_4 = Button(win,text = "4", width=10, command = four)
# b_4.grid(row = 1, column = 0)

# b_5 = Button(win,text = "5", width=10, command = five)
# b_5.grid(row = 1, column = 1)

# b_6 = Button(win,text = "6", width=10, command = six)
# b_6.grid(row = 1, column = 2)

# b_7 = Button(win,text = "7", width=10, command = seven)
# b_7.grid(row = 2, column = 0)

# b_8 = Button(win,text = "8", width=10, command = eight)
# b_8.grid(row = 2, column = 1)

# b_9 = Button(win,text = "9", width=10, command = nine)
# b_9.grid(row = 2, column = 2)

# b_0 = Button(win,text = "0", width=10, command = zero)
# b_0.grid(row = 3, columnspan = 4, sticky = "ew")

# win.mainloop()

