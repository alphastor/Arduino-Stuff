#-----------import GUI builder module and a py file stored in same directory-----------#
import os
from tkinter import *
from display1 import *

#-----------clear terminal before every run-----------#
os.system('cls')

#-----------variable to store result of calculation-----------#
result=0


#-----------dictionaries to store functions in display1.py file-----------#
funcs_1 = {'0': zero, '1': one, '2': two, '3': three, '4': four,
           '5': five, '6': six, '7': seven, '8': eight, '9': nine, '-': minus}
keys_1 = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '-']

funcs_2 = {'0_2': zero_2, '1_2': one_2, '2_2': two_2, '3_2': three_2, '4_2': four_2,
           '5_2': five_2, '6_2': six_2, '7_2': seven_2, '8_2': eight_2, '9_2': nine_2}
keys_2 = ['0_2', '1_2', '2_2', '3_2', '4_2', '5_2', '6_2', '7_2', '8_2', '9_2']


#-----------functions-----------#
def num(x): # --display value of pressed button-- #
    if screen.get() == '0':
        clear_display()
        screen.delete(0, 'end') # --delete num at the zero_th index and end default val of end is empty str -- #
        screen.insert(0, str(x))
    else:
        clear_display()
        length = len(screen.get())
        screen.insert(length, str(x)) # --add the pressed number ie str(x) before whatever num/operator present-- #

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

def other_btns(): # --adding other to the window-- #
    btn_off = Button(win, width=6, text='off', bd=0, height=2, bg='#D3D3D3', command=off)
    btn_off.place(x=30, y=70)

    btn_clear = Button(win, width=6, text='C', bd=0, height=2,bg='#D3D3D3', command=clear)
    btn_clear.place(x=82, y=70)

    btn_delete = Button(win, width=6, text='⌫', bd=0, height=2,bg='#D3D3D3', command=delete)
    btn_delete.place(x=134, y=70)

    btn_calculate = Button(win, width=6, text='=', bd=0, height=2,bg='#D3D3D3', command=cal_n_display_result)
    btn_calculate.place(x=186, y=230)

def clear():
    screen.delete(0, 'end') # --delete everything strting from 0 till end-- #
    screen.insert(0,'0')

    clear_display()

def delete():
    length = len(screen.get())
    screen.delete(length-1, 'end')
    if length == 1:
        screen.insert(0,'0')

def opr(x):
    if screen.get() != '0':
        length = len(screen.get())
        screen.insert(length, operator[x]['text'])

def cal_n_display_result():
    usr_input = screen.get()
    result = eval(usr_input)
    # screen.delete(0, 'end')
    # screen.insert(0, result)

    a = str(result)
    b = a[0]

    if len(a) == 2:
            if b == "-":
                funcs_1[keys_1[10]]()
                funcs_2[keys_2[int(a[1])]]()
            else:
                num_1 = int(b)
                num_2 = int(a[1])
                funcs_1[keys_1[num_1]]()
                funcs_2[keys_2[num_2]]()
    elif len(a) == 1:
        funcs_1[keys_1[0]]()
        funcs_2[keys_2[result]]()

#-----------initialise window-----------#
win = Tk()  # --provides a robust and platform independent windowing toolkit-- #
win.title("Display result on 7 Segment")  # --naming the window-- #

win.geometry("265x280+1230+100") # --widthxheight+posx+posy posx&y is where on the screen window should open-- #
win.maxsize(265, 280) # --max window resize-- #
win.minsize(265, 280) # --min window resize-- #

lbl = Label(win, text="-------✗Standard✗-------", font='AnaEve')  # --display a text in window-- #
lbl.place(x=8, y=5)

screen = Entry(win, width=18, bd=0, font='10', bg='#D3D3D3', justify=RIGHT) # --initialise screen to display ans-- #
screen.insert(0, '0')
screen.place(x=30, y=40)  # --positioning the screen-- #

#-----------operator buttons-----------#
operator = []
for i in range(4):
    operator.append(Button(win, width=6, bd=0, height=2, bg='#D3D3D3', command=lambda x=i:opr(x)))

operator[0]['text'] = '+'
operator[1]['text'] = '-'
operator[2]['text'] = '*'
operator[3]['text'] = '/'

for i in range(4):
    operator[i].place(x=186, y=70+i*40)

#-----------calling the functions-----------#
number_btns()
other_btns()

win.mainloop()  # --run above codes in a loop till window is closed-- #