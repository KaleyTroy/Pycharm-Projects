from tkinter import *

class NameArray(Entry):
    def __init__(self, args):
        super(NameArray, self).__init__()
        self.config(font=('papyrus', 20, 'normal'))
        self.insert(0, f"TM {args['rank']}")
        self.grid(row=args["rank"], column=args["file"], padx=10, pady=10)

class ButtonArray(Button):
    def __init__(self, args):
        super().__init__()
        self.config(text=args["type"], font=('papyrus', 20, 'normal'))
        self.grid(row=args["rank"], column=args["file"], padx=10, pady=10)