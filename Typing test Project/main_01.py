from tkinter import *
from connectnano import *

import os
os.system('cls')


func = {97:char_A}
keyz = [97]

def keys(event):
    key = event.char
    # print(key)
    # print(ord(key))
    func.get(ord(key))()

#----------Window initialising----------#
win = Tk()
win.iconbitmap(r'D:\VS Code\P R O J E C T S\Arduino Stuff\Typing test Project\myicon.ico') #--r is to tell that its a path--#
win.title('Typing Test Game')
win.geometry('100x50+1250+100')
win.bind("<Key>", keys)

win.mainloop()
