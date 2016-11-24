# -*-coding:utf-8 -*-
import tkinter as tk
root = tk.Tk()
w = 200 # width for the Tk root
h = 250 # height for the Tk root
ws = root.winfo_screenwidth() # width of the screen
hs = root.winfo_screenheight() # height of the screen
x = ws - w - 20
y = hs - h - 80

data =[]
print('%dx%d+%d+%d' % (w, h, x, y))
# set the dimensions of the screen
# and where it is placed
root.geometry('%dx%d+%d+%d' % (w, h, x, y))
#root.configure(background='gold')
root.call('wm', 'attributes', '.', '-topmost', '1')
root.lift()
# write list
listbox = tk.Listbox(root)
listbox.pack()

#listbox.delete(2, 'end')
def render():
    for item in data:
        listbox.insert('end', item)

def task():
    data.append('a')
    render()
    root.after(5, task)

root.after(1, task)

root.mainloop() # starts the mainloop
