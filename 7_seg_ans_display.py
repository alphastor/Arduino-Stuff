import pyfirmata as pf
from tkinter import *

a = 3
b = 2
c = 8
d = 7
e = 6
f = 4
g = 5

seg_7 = pf.Arduino("COM5")

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

