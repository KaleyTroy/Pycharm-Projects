from tkinter import *

app = Tk()
app.title("cm to inch cockverter")
app.minsize(width=300, height=150)
app.config(padx=30, pady=30)

def fuck_us(event):
    event.widget.select_range(0, "end")

def inch_to_cm():
    cock_cm.delete(0, 'end')
    cm = cock_inch.get().split(" ")
    cm = round(float(cm[0]) * 2.54, 2)
    cock_cm.insert(END, string=f"{cm} centimeters!")

def cm_to_inch():
    cock_inch.delete(0, 'end')
    inch = cock_cm.get().split(" ")
    inch = round(float(inch[0]) / 2.54, 2)
    cock_inch.insert(END, string=f"{inch} inches!")


cock_inch = Entry(width=20)
cock_inch.insert(END, string="Cock inches")
cock_inch.bind("<FocusIn>", fuck_us)
cock_inch.grid(column=0, row=0)

cock_cm = Entry(width=20)
cock_cm.insert(END, string="Cock centimeters")
cock_cm.bind("<FocusIn>", fuck_us)
cock_cm.grid(column=1, row=0)

inch_to_cm_button = Button(text=">>", command=inch_to_cm)
inch_to_cm_button.grid(column=0, row=1)
cm_to_inch_button = Button(text="<<", command=cm_to_inch)
cm_to_inch_button.grid(column=1, row=1)


app.mainloop()
