from tkinter import *
from datetime import *
from elements import *

the_app = Tk()
today = "Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday".split(", ")
today = today[datetime.now().weekday()]
ticket_type = "1, 2, IMS, INC, TASK".split(", ")

button = []
for rank in range(2, 8):
    for file in range(2, 5):
        button.append(ButtonArray({'rank': rank, 'file': file, 'type': ticket_type[file]}))


the_app.mainloop()
