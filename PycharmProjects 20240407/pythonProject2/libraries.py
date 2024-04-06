from csv import *
from datetime import *
from tkinter import *
from re import *
import webbrowser as web
from fractions import *

URL = [
    'https://bunnings.service-now.com/now/workspace/agent/list/params/list-id/f63700d8db95e9103962b6f5f3961952/tiny/624dc93a879125500e6931140cbb35ec'
    'https://bunnings.service-now.com/now/workspace/agent/list/params/list-id/2b9ccd3a879125500e6931140cbb3548/tiny/c9ec4d3a879125500e6931140cbb35e4'
    'https://bunnings.service-now.com/now/workspace/agent/list/params/list-id/ce7e45ba879125500e6931140cbb35fa/tiny/467e05ba879125500e6931140cbb3558']
APPLET = Tk(); APPLET.config(padx=5, pady=5, borderwidth=10)
APPLET.title("Distributor")
APPLET.geometry("+2000+-10")
ROOT = "C:\\Users\\Luke\\OneDrive\\Distributor\\"
TYPE = ["Interaction", "Incident", "Task"]
TYP = ["IMS", "INC", "TAS"]
clean = [], [], []
button = []; radio = []; entry = []; radio_var = IntVar(value=2)
ACTIVE_TM = 2; ACTIVE_TYPE = 1


tickets = ["", "", ""]
for cycle in range(3):
    with open(f"{ROOT}Overnight {TYPE[cycle]} Report TEST.csv") as f: raw = list(reader(f))
    for row in raw: clean[cycle].append([row[0], sub(r'^(fw:|re:)\s*', '', (row[1].lower()))])
    clean[cycle].sort(key=lambda row: row[1])
    for x in clean[cycle]: tickets[cycle] += str(x[0] + ",\n")
    tickets[cycle] = tickets[cycle].split("\n")
    print(tickets[cycle])


class ButtonArray(Button):
    active_tm = 2
    active_type = 2

    def __init__(self, x, y):
        super().__init__()
        self.config(text=TYP[x-1], width=5, font=('Arial', 20, 'normal'),
                    borderwidth=3, padx=0, pady=0, command=self.clicked)
        self.grid(row=y, column=x, padx=5, pady=5)
        self.type = TYP[x-1]
        self.team_member = y

    def clicked(self):
        ButtonArray.active_tm = self.team_member
        ButtonArray.active_type = self.type


class RadioArray(Radiobutton):
    def __init__(self, y):
        super(RadioArray, self).__init__()
        self.config(variable=radio_var, value=y, command=self.radio_changed)
        self.grid(row=y, column=4, padx=5)

    def radio_changed(self):
        print(radio_var.get())


class EntryArray(Entry):

    def __init__(self, grid_y):
        super(EntryArray, self).__init__()
        self.config(font=('Arial', 20, 'normal'), width=16)
        self.grid(row=grid_y, column=5, padx=5)
        self.name = f"Team Member {grid_y}"
        self.insert(0, self.name)

class Texties(Text):
    def __init__(self):
        super(Texties, self).__init__()
        self.config(width=30, height=18, font=('Arial', 16, 'normal'))
        self.grid(row=1, column=6, columnspan=2, rowspan=6, padx=15, pady=15)

class Header(Entry):
    def __init__(self):
        super(Header, self).__init__()
        self.config(width=26, font=('Arial', 30, 'normal'))
        self.grid(row=0, column=0, columnspan=10)

class Leavers(Button):
    def __init__(self):
        super(Leavers, self).__init__()
        self.config(text="Exit", width=10, font=('Arial', 20, 'normal'),
                    borderwidth=3, padx=0, pady=0, command=self.quit_click)
        self.grid(row=7, column=0, columnspan=4)

    def quit_click(self):
        APPLET.destroy()

class Goer(Button):
    def __init__(self):
        super(Goer, self).__init__()
        self.config(text="Go", width=10, font=('Arial', 20, 'normal'),
                    borderwidth=3, padx=0, pady=0, command=self.go_click)
        self.grid(row=7, column=6, columnspan=2)

    def go_click(self):
        web.open(URL[ButtonArray.ticket_type])
