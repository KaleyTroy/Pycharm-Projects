from tkinter import *
from tkinter import messagebox as mb
import json
from random import *

# ---------------------------- FULL QUIT ------------------------------- #
def full_quit():
    canvas.destroy()
    root.destroy()


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    password = []
    chars = "qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM1234567890!@#$%^&*()"
    splits = (0, 26), (26, 52), (52, 62), (62, 71), (0, 71), (0, 71), (0, 71), (0, 71)
    for not_x in range(randint(12, 24)): password += [chars[randint(*splits[not_x % 8])]]
    shuffle(password); box_variable[2].set("".join(password))
    update()

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save(message=""):
    global box_variable; saves = {}; jason = {}
    for f_txt_index, f_txt_value in enumerate(txt): saves[f_txt_value] = box_variable[f_txt_index].get().replace(" ", "")
    for f_key, f_txt_value in saves.items(): message += f"\n{f_key} {f_txt_value}"
    jason[saves[txt[0]]] = saves
    if mb.askokcancel(title="Saving...", message=f"Save this key?{message}?"):
        try:
            with open("jason.json", 'r') as f: data = json.load(f); data.update(jason)
            with open("jason.json", 'w') as f: json.dump(data, f, indent=4)
        except FileNotFoundError:
            with open("jason.json", 'w') as f: json.dump(jason, f, indent=4)

        box_entry[0].delete(0, END); box_entry[2].delete(0, END)
        mb.showinfo(title="Saved", message="Key saved successfully!")

# ---------------------------- SEARCH ------------------------------- #
def search():
    try:
        with open("jason.json", 'r') as f: jason = json.load(f)
        jason.update(jason)
        found = jason[box_variable[0].get()]
        for x, (y, z) in enumerate(found.items()):
            print(x); print(y); print(z)
            box_variable[x].set(z)
    except (NameError, FileNotFoundError, KeyError):
        print("noooope")

# ---------------------------- UPDATE ------------------------------- #
def update(*args, user_input=0):
    for text in box_variable: user_input += text.get().strip() == ""
    if user_input or len(box_variable[1].get().split("@")) == 1: add.config(state='disabled')
    else: add.config(state='active')

# ---------------------------- UI SETUP ------------------------------- #
# === Variables ===
txt = "Website:,Email/Username:,Password:".split(",")
root = Tk(); root.title("Penis"); root.config(padx=20, pady=20)
canvas = Canvas(width=200, height=200); butt_hole = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=butt_hole); canvas.grid(row=0, column=1)
lbl, box_entry, box_variable = [], [], []

# === Widgets ===
for txt_index, txt_value in enumerate(txt):
    lbl.append(Label(text=txt_value)); lbl[txt_index].grid(row=txt_index + 1, column=0, sticky='snew', padx=3, pady=3)
    box_variable.append(StringVar())
    box_entry.append(Entry(width=32, textvariable=box_variable[txt_index]))
    box_entry[txt_index].grid(row=txt_index + 1, column=1, padx=3, pady=3)
    for x in ['<FocusOut>', '<Button>']: box_entry[txt_index].bind(x, update)

# === Buttons ===
search = Button(width=15, text="Search", command=search); search.grid(row=1, column=2, padx=3, pady=3)
email = Button(width=15, text="Default Email", command=lambda: box_variable[1].set("example@penis.com")); email.grid(row=2, column=2, padx=3, pady=3)
gen = Button(width=15, text="Generate Password", command=generate_password); gen.grid(row=3, column=2, padx=3, pady=3)
full_exit = Button(width=15, text="Exit", command=full_quit); full_exit.grid(row=4, column=2, padx=3, pady=3)
add = Button(text="Add", width=26, command=save); add.grid(row=4, column=1, columnspan=1, padx=3, pady=3)


generate_password()
mainloop()
