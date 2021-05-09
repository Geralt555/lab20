#!/usr/bin/env python3
# -*- config: utf-8 -*-

# напишите программу по следующему описанию. Нажатие Enter в
# однострочном текстовом поле приводит к перемещению текста из него в список (экземпляр
# Listbox ). При двойном клике ( <Double-Button-1> ) по элементу-строке списка, она должна
# копироваться в текстовое поле.

from tkinter import *

root = Tk()


def take_item():
    s = e.get()
    e.delete(0, END)
    l.insert(END, s)


def give_item():
    tup = l.curselection()
    if tup:
        s = l.get(tup[0])
        e.delete(0, END)
        e.insert(0, s)


e = Entry()
e.pack()
e.bind('<Return>', take_item)
l = Listbox()
l.pack()
l.bind('<Double-Button-1>', give_item)
root.mainloop()
