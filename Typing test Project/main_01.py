# from tkinter import *
from connectnano import *
from keyboard import *
from time import sleep

import os
os.system('cls')

func = {97:A, 98:B, 99:C, 100:D,
        101:E, 102:F, 103:G, 104:H, 105:I, 106:J, 107:K, 108:L, 109:M, 110:N,
        111:O, 112:P, 113:Q, 114:R, 115:S, 116:T, 117:U, 118:V, 119:W,
        120:X, 121:Y, 122:Z
       }

while True:
    if is_pressed('a'):
        func.get(ord('a'))()

    if is_pressed('b'):
        func.get(ord('b'))()

    if is_pressed('c'):
        func.get(ord('c'))()

    if is_pressed('d'):
        func.get(ord('d'))()

    if is_pressed('e'):
        func.get(ord('e'))()

    if is_pressed('f'):
        func.get(ord('f'))()

    if is_pressed('g'):
        func.get(ord('g'))()

    if is_pressed('h'):
        func.get(ord('h'))()

    if is_pressed('i'):
        func.get(ord('i'))()

    if is_pressed('j'):
        func.get(ord('j'))()

    if is_pressed('k'):
        func.get(ord('k'))()

    if is_pressed('l'):
        func.get(ord('l'))()

    if is_pressed('m'):
        func.get(ord('m'))()

    if is_pressed('n'):
        func.get(ord('n'))()

    if is_pressed('o'):
        func.get(ord('o'))()

    if is_pressed('p'):
        func.get(ord('p'))()

    if is_pressed('q'):
        func.get(ord('q'))()

    if is_pressed('r'):
        func.get(ord('r'))()

    if is_pressed('s'):
        func.get(ord('s'))()

    if is_pressed('t'):
        func.get(ord('t'))()

    if is_pressed('u'):
        func.get(ord('u'))()

    if is_pressed('v'):
        func.get(ord('v'))()

    if is_pressed('w'):
        func.get(ord('w'))()

    if is_pressed('x'):
        func.get(ord('x'))()

    if is_pressed('y'):
        func.get(ord('y'))()

    if is_pressed('z'):
        func.get(ord('z'))()

###############################################################################
# def keys(event):
#     key = event.char
#     func.get(ord(key))()

#----------Window initialising----------#
# win = Tk()
# win.iconbitmap(r'D:\VS Code\P R O J E C T S\Arduino Stuff\Typing test Project\myicon.ico') #--r is to tell that its a path--#
# win.title('Typing Test Game')
# win.geometry('100x50+1250+100')
# win.bind("<Key>", keys)

# win.mainloop()

###################################################################################

# from tkinter import *

# running = True  # Global flag

# def scanning():
#     if running:  # Only do this if the Stop button has not been clicked
#         print ("hello")

#     # After 1 second, call scanning again (create a recursive loop)
#     root.after(100, scanning)

# def start():
#     """Enable scanning by setting the global flag to True."""
#     global running
#     running = True

# def stop():
#     """Stop scanning by setting the global flag to False."""
#     global running
#     running = False

# root = Tk()
# root.title("Title")
# root.geometry("500x500")

# app = Frame(root)
# app.grid()

# start = Button(app, text="Start Scan", command=start)
# stop = Button(app, text="Stop", command=stop)

# start.grid()
# stop.grid()

# root.after(1000, scanning)  # After 1 second, call scanning
# root.mainloop()