#!/usr/bin/env python3
# -*- config: utf-8 -*-

# в данной программе создается анимация круга, который движется от левой
# границы холста до правой:

from tkinter import *


def motion():
    c.move(ball, 1, 0)
    if c.coords(ball)[2] < 300:
        root.after(10, motion)


root = Tk()
c = Canvas(root, width=300, height=200,
           bg="white")
c.pack()
ball = c.create_oval(0, 100, 40, 140,
                     fill='green')
motion()
root.mainloop()
