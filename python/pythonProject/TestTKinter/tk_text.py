# -*-coding:utf-8 -*-
import tkinter as tk
root = tk.Tk()
text = tk.Text(root)
text.insert('insert', "hello")
text.insert("insert", 'world')
text.insert('insert', 'wifi')
text.insert('insert', 'hehe')
text.pack()
root.mainloop()