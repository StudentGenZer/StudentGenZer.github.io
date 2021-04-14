from tkinter import *
import random

def func_1():
    txt["text"]+="1"

def func_2():
    txt["text"]+="2"

def func_3():
    txt["text"]+="3"

def func_4():
    txt["text"]+="4"

def func_5():
    txt["text"]+="5"

def func_6():
    txt["text"]+="6"

def func_7():
    txt["text"]+="7"

def func_8():
    txt["text"]+="8"

def func_9():
    txt["text"]+="9"

def func_plus():
    txt["text"]+="+"

def func_0():
    txt["text"]+="0"

def func_minus():
    txt["text"]+="-"

def eqv():
    txt["text"] = str(eval(txt["text"]))

def clear_text():
    txt["text"] = ""
    

root = Tk()
root.title("Star")
root.geometry("380x760")


txt = Label(root, text = "", font = "Arial 30")
txt.place(x = 20, y = 50)

but_1 = Button(root, text = "1", font = "Arial 20", command = func_1)
but_1.place(x = 20, y = 160, width = 100, height = 100)
but_2 = Button(root, text = "2", font = "Arial 20", command = func_2)
but_2.place(x = 140, y = 160, width = 100, height = 100)
but_3 = Button(root, text = "3", font = "Arial 20", command = func_3)
but_3.place(x = 260, y = 160, width = 100, height = 100)


but_4 = Button(root, text = "4", font = "Arial 20",command = func_4)
but_4.place(x = 20, y = 280, width = 100, height = 100)
but_5 = Button(root, text = "5", font = "Arial 20",command = func_5)
but_5.place(x = 140, y = 280, width = 100, height = 100)
but_6 = Button(root, text = "6", font = "Arial 20", command = func_6)
but_6.place(x = 260, y = 280, width = 100, height = 100)

but_7 = Button(root, text = "7", font = "Arial 20", command = func_7)
but_7.place(x = 20, y = 400, width = 100, height = 100)
but_8 = Button(root, text = "8", font = "Arial 20", command = func_8)
but_8.place(x = 140, y = 400, width = 100, height = 100)
but_9 = Button(root, text = "9", font = "Arial 20", command = func_9)
but_9.place(x = 260, y = 400, width = 100, height = 100)

but_plus = Button(root, text = "+", font = "Arial 20", command = func_plus)
but_plus.place(x = 20, y = 520, width = 100, height = 100)
but_0 = Button(root, text = "0", font = "Arial 20", command = func_0)
but_0.place(x = 140, y = 520, width = 100, height = 100)
but_minus = Button(root, text = "-", font = "Arial 20", command = func_minus)
but_minus.place(x = 260, y = 520, width = 100, height = 100)

but_eqvl = Button(root, text = "=", font = "Arial 20", command = eqv)
but_eqvl.place(x = 20, y = 640, width = 100 , height = 100)

but_clear = Button(root, text = "C", font = "Arial 20", fg = "red",command = clear_text)
but_clear.place(x = 140, y = 640, width = 100 , height = 100)
root.bind("1",func_1)

root.mainloop()
