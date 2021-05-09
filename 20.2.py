#!/usr/bin/env python3
# -*- config: utf-8 -*-

# напишите программу по описанию. Размеры многострочного текстового
# поля определяются значениями, введенными в однострочные текстовые поля. Изменение
# размера происходит при нажатии мышью на кнопку, а также при нажатии клавиши Enter.
# Цвет фона экземпляра Text светлосерый ( lightgrey ), когда поле не в фокусе, и белый,
# когда имеет фокус.

from tkinter import *

root = Tk()


def change_side():
    if ew.get().isdigit():
        t['width'] = ew.get()
    if eh.get().isdigit():
        t['height'] = eh.get()


def white_color():
    t['bg'] = 'white'


def grey_color():
    t['bg'] = 'lightgrey'


f1 = Frame()
f1.pack()
f = Frame(f1)
f.pack(side=LEFT)
ew = Entry(f, width=3)
ew.pack()
ew.focus_set()
eh = Entry(f, width=3)
eh.pack()
b = Button(f1, text="Преобразовать")
b.pack(side=LEFT)
b.bind('<Button-1>', change_side)
b.bind('<Return>', change_side)
ew.bind('<Return>', change_side)
eh.bind('<Return>', change_side)
f2 = Frame()
f2.pack()
t = Text(f2, width=20, height=10, bg='lightgrey')
t.pack()
t.bind('<FocusIn>', white_color)
t.bind('<FocusOut>', grey_color)
root.mainloop()
