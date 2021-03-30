#-----------import GUI builder module and a py file stored in same directory-----------#
import os
from tkinter import *
# from display1 import *

#-----------clear terminal before every run-----------#
os.system('cls')

#-----------initialise window-----------#
win = Tk()  # --provides a robust and platform independent windowing toolkit-- #
win.title("Display result on 7 Segment")  # --naming the window-- #

win.geometry("265x280+1230+100") # --widthxheight+posx+posy posx&y is where on the screen window should open-- #
win.maxsize(265, 280) # --max window resize-- #
win.minsize(265, 280) # --min window resize-- #

lbl = Label(win, text="-------✗Standard✗-------", font='AnaEve')  # --display a text in window-- #
lbl.place(x=8, y=5)

def num(x): # --display value of pressed button-- #
    if screen.get() == '0':
        screen.delete(0, 'end') # --delete num at the zero_th index and end default val of end is empty str -- #
        screen.insert(0, str(x))
    else:
        length = len(screen.get())
        screen.insert(length, str(x)) # --add the pressed number ie str(x) before whatever num/operator present-- #

screen = Entry(win, width=18, bd=0, font='10', bg='#D3D3D3', justify=RIGHT) # --initialise screen to display ans-- #
screen.insert(0, '0')
screen.place(x=30, y=40)  # --positioning the screen-- #

def number_btns(): # --adding buttons to the window with a loop-- #
    buttons = []
    for i in range(10):
        buttons.append(Button(win, width=6, text=str(i), bd=0, height=2, bg='#D3D3D3', command=lambda x=i: num(x)))
    btn_txt = 1
    for i in range(0, 3):
        for j in range(0, 3):
            buttons[btn_txt].place(x=30+j*52, y=110+i*40)
            btn_txt += 1
    btn_zero = Button(win, width=21, text='0', bd=0, height=2, bg='#D3D3D3', command=lambda x=0: num(x))
    btn_zero.place(x=30, y=230)
def operator_btns(): # --adding operators to the window-- #
    btn_none = Button(win, width=6, text='none', bd=0, height=2, bg='#D3D3D3')
    btn_none.place(x=30, y=70)

    btn_clear = Button(win, width=6, text='C', bd=0, height=2,bg='#D3D3D3')
    btn_clear.place(x=82, y=70)

    btn_delete = Button(win, width=6, text='⌫', bd=0, height=2,bg='#D3D3D3')
    btn_delete.place(x=134, y=70)

    btn_decimal = Button(win, width=6, text='.', bd=0, height=2,bg='#D3D3D3')
    btn_decimal.place(x=186, y=230)

    operator = []
    for i in range(4):
        operator.append(Button(win, width=6, bd=0, height=2, bg='#D3D3D3'))

    operator[0]['text'] = '+'
    operator[1]['text'] = '-'
    operator[2]['text'] = '×'
    operator[3]['text'] = '÷'

    for i in range(4):
        operator[i].place(x=186, y=70+i*40)

number_btns()
operator_btns()

win.mainloop()  # --run above codes in a loop till window is closed-- #