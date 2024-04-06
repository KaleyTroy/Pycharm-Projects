from csv import *
from datetime import *
from re import *
from tkinter import *
from tkinter import filedialog as fd
from tkinter import messagebox as mb

URL = [
    "https://bunnings.service-now.com/now/workspace/agent/list/params/list-id/f63700d8db95e9103962b6f5f3961952/tiny/d6efc85887b9a9906178ec270cbb3546",
    "https://bunnings.service-now.com/now/workspace/agent/list/params/list-id/2b9ccd3a879125500e6931140cbb3548/tiny/1010909887b9a9906178ec270cbb35c7",
    "https://bunnings.service-now.com/now/workspace/agent/list/params/list-id/ce7e45ba879125500e6931140cbb35fa/tiny/a940149887b9a9906178ec270cbb35ff"]

TYPE = ["Interaction", "Incident", "Task"]
TYP = ["IMS", "INC", "TAS"]
root, font_l, font_s = Tk(), ("Arial", 20, "normal"), ("Arial", 14, "normal")
root.config(padx=25, pady=0, borderwidth=10)
# root.geometry("+2000+-10")
root.title("Distributor")
ims, inc, tas, radio, name_space, name_label = [], [], [], [], [], []
radio_var = IntVar(value=2)
tickets = ["", "", ""]
the_day = f"{date.today().strftime('%A')}"
CANCEL = False

def file_sort_default():
    clean = [], [], []
    try:
        with open("directory.txt", "r") as file: root_dir = file.read()
        for cycle in range(3):
            with open(f"{root_dir}/Overnight {TYPE[cycle]} Report.csv") as f: raw = list(reader(f))
            for row in raw: clean[cycle].append([row[0], sub(r'^(fw:|re:)\s*', '', (row[1].lower()))])
            clean[cycle].sort(key=lambda row: row[1])
            tickets[cycle] = ""
            for x in clean[cycle]: tickets[cycle] += str(x[0] + ",\n")
            tickets[cycle] = tickets[cycle].replace("number,\n", "")
            tickets[cycle] = tickets[cycle].split("\n")
            del tickets[cycle][len(tickets[cycle]) - 1]
    except Exception:
        file_sort()

def file_sort():
    global CANCEL
    clean = [], [], []
    root_dir = str(fd.askdirectory())
    if root_dir == "": root.destroy(); return

    try:
        for cycle in range(3):
            with open(f"{root_dir}/Overnight {TYPE[cycle]} Report.csv") as f: raw = list(reader(f))
            for row in raw: clean[cycle].append([row[0], sub(r'^(fw:|re:)\s*', '', (row[1].lower()))])
            clean[cycle].sort(key=lambda row: row[1])
            tickets[cycle] = ""
            for x in clean[cycle]: tickets[cycle] += str(x[0] + ",\n")
            tickets[cycle] = tickets[cycle].replace("number,\n", "")
            tickets[cycle] = tickets[cycle].split("\n")
            del tickets[cycle][len(tickets[cycle]) - 1]
        with open("directory.txt", "w") as file: file.write(root_dir)
    except Exception:
        mb.showerror("Error", "Invalid directory selected. Please choose a different folder.")
        file_sort()
    print(f"{root_dir}/Overnight {TYPE[cycle]} Report.csv")
file_sort_default()
