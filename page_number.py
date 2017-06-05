from tkinter import *
from math import *
def jump(event):
    try:
        page_input = int(entry.get())
        print(str(page_input))
    except:
        pass

root = Tk()
Label(root, text="Page Number:").grid(row=0)
entry = Entry(root)
entry.grid(row=0, column=1)
entry.bind("<Return>", jump)
root.mainloop()