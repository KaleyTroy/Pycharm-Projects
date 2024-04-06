lockers = """
     ____
    /  _ \ 
   ( /  ) |
   | |  (^)
 __|_|_______
<___________>\
| |         ||
| |         ||
| |         ||
| |         ||
| |         ||
| |         ||
\_|_________|/
 """
from tkinter import *

import butthole
fonty = ("Arial", 20, "normal")

def balls(an_argument):
    butthole.label.config(text=butthole.enter.get())

def texy_boy():
    butthole.label.config(text="You flicked my button")

root = Tk()
root.geometry("200x200+2000-600")
button = Button(text="Button", command=texy_boy, font=fonty)
button.pack()
label = Label(text="This is a label", font=fonty)
label.pack()
enter = Entry()
enter.pack()
enter.bind("<KeyRelease>", balls)

label1 = Label()
label1.config(text=lockers)
label1.pack(a)

mainloop()