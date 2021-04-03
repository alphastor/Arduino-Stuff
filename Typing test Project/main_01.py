# from tkinter import *
from connectnano import *
from keyboard import *
from time import sleep

import os
os.system('cls')

func = {97:char_A, 98:char_B, 99:char_C, 100:char_D}
# keyz = func.keys()

while True:
    if is_pressed('a'):
        func.get(ord('a'))()
    if is_pressed('b'):
        func.get(ord('b'))()
    if is_pressed('c'):
        func.get(ord('c'))()
    if is_pressed('d'):
        func.get(ord('d'))()
    # if is_pressed('e'):
        # func.get(ord('e'))()
    # if is_pressed('f'):
        # func.get(ord('f'))()
    # if is_pressed('g'):
        # func.get(ord('g'))()

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