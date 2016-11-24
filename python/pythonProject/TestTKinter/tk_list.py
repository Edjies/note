# -*-coding:utf-8 -*-
import tkinter as tk

top = tk.Tk()

Lb1 = tk.Listbox(top)
for i in range(10):
    Lb1.insert(i, '{}  {}  {}'.format('00700' + str(i), '0.23' + str(i), '0.24' + str(i)))

Lb1.pack()
top.mainloop()