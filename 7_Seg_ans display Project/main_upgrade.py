#-----------import GUI builder module and a py file stored in same directory-----------#
from tkinter import *
# from display1 import *

#-----------initialise window-----------#
win = Tk()  # --provides a robust and platform independent windowing toolkit-- #
win.title("Answer Display")  # --naming the window-- #

win.geometry("300x500+900+150") # --widthxheight+posx+posy posx&y is where on the screen window should open-- #

lbl = Label(win, text="---------✗alphastor✗---------", font='AnaEve')  # --display a text in window-- #
lbl.place(x=6, y=5)

screen = Entry(win, width=25, bd=1, font='10') # --initialise screen to display ans-- #
screen.place(x=30, y=40)  # --positioning the screen-- #

# --adding buttons to the window with a loop-- #
buttons = []
for i in range(10):
    buttons.append(Button(width=7, text=str(i), bd=1, height=2))
btn_txt = 1
for i in range(0, 3):
    for j in range(0, 3):
        buttons[btn_txt].place(x=30+j*60, y=70+i*40)
        btn_txt += 1

win.mainloop()  # --run above codes in a loop till window is closed-- #