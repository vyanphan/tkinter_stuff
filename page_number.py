from tkinter import *
from math import *
def jump(event):
    try:
        page_input = int(entry.get())
        print(str(page_input))
    except:
        pass

w = Tk()
Label(w, text="Page Number:").grid(row=0)
entry = Entry(w)
entry.grid(row=0, column=1)
entry.bind("<Return>", jump)
w.mainloop()