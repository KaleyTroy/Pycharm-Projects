import random as rn, csv
from tkinter import *
BG_COLOUR = "#B1DDC6"

def f_tick(*args): canvas_front.grid()
def f_cross(*args): canvas_front.grid_remove()
def f_close(*args): root.destroy()
def new_card():
    with open ("words.csv", 'r') as f: f = list(csv.reader(f))
    active_card = f[rn.randint(0, 100)]
    spanish_word_var.set(active_card[0])
    english_word_var.set(active_card[1])
    points_var.set(active_card[3])
    f_tick()

root = Tk(); root.config(padx=50, pady=50, width=800, height=526, bg=BG_COLOUR); root.bind('<Escape>', f_close)
canvas_back = Canvas(width=800, height=526, bg=BG_COLOUR, borderwidth=0, highlightthickness=0); card_back = PhotoImage(file="images/card_back.png")
canvas_back.create_image(400, 263, image=card_back); canvas_back.grid(row=0, column=0, columnspan=3, pady=15)
english_word_var = StringVar(value="English Word")
english_word_lbl = Label(canvas_back, font=("Arial", 30, "normal"), textvariable=english_word_var, bg="white")
canvas_back.create_window(400, 200, window=english_word_lbl)
new_card_button = Button(canvas_back, text="Next card", command=new_card)
canvas_back.create_window(400, 400, window=new_card_button)

canvas_front = Canvas(width=800, height=526, bg=BG_COLOUR, borderwidth=0, highlightthickness=0)
card_front = PhotoImage(file="images/card_front.png")
canvas_front.create_image(400, 264, image=card_front)
canvas_front.grid(row=0, column=0, columnspan=3, pady=15)
spanish_word_var = StringVar(value="Spanish Word"); points_var = StringVar(value="Points"); guess_var = StringVar()
spanish_word_lbl = Label(canvas_front, font=("Arial", 30, "normal"), textvariable=spanish_word_var, bg="white")
points_lbl = Label(canvas_front, textvariable=points_var, font=("Arial", 20, "normal"), bg="white")
canvas_front.create_window(400, 200, window=spanish_word_lbl)
canvas_front.create_window(400, 300, window=points_lbl)

# guess_ent = Entry(canvas_front, textvariable=guess_var)
# word_lbl.grid(row=1, column=1); point_lbl.grid(row=2, column=1); guess_ent.grid(row=3, column=1)


green_tick = PhotoImage(file="images/right.png"); correct_button = Button(command=f_tick, image=green_tick, borderwidth=2); correct_button.grid(row=2, column=2, pady=15, sticky="s")
red_cross = PhotoImage(file="images/wrong.png"); incorrect_button = Button(command=f_cross, image=red_cross, borderwidth=2); incorrect_button.grid(row=2, column=0, pady=15, sticky="s")
entry = Entry(foreground=BG_COLOUR, font=('Arial', 20, 'normal')); entry.grid(row=2, column=1); entry.bind("<Return>", f_cross)

new_card()
mainloop()
