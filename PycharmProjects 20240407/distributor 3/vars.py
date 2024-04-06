from csv import *
from datetime import *
from re import *
from tkinter import *
from tkinter import messagebox as mb
from tkinter import filedialog as fd
import webbrowser as link
import pyperclip as cb
import sys
import threading
import sys

from random import randint

URL = [
    "https://bunnings.service-now.com/now/workspace/agent/list/params/list-id/f63700d8db95e9103962b6f5f3961952/tiny/d6efc85887b9a9906178ec270cbb3546",
    "https://bunnings.service-now.com/now/workspace/agent/list/params/list-id/2b9ccd3a879125500e6931140cbb3548/tiny/1010909887b9a9906178ec270cbb35c7",
    "https://bunnings.service-now.com/now/workspace/agent/list/params/list-id/ce7e45ba879125500e6931140cbb35fa/tiny/a940149887b9a9906178ec270cbb35ff"]

root, large, small = Tk(), ("Arial", 20, "normal"), ("Arial", 14, "normal")
root.config(padx=25, pady=0, borderwidth=10); root.title("Distributor")
TYPE = ["Interaction", "Incident", "Task"]; TYP = ["IMS", "INC", "TAS"]
tms, ims, inc, tas, radio, name_space, name_var, array = [], [], [], [], [], [], [], []
radio_var, the_day = IntVar(value=6), f"{date.today().strftime('%A')}"

def task_sort():
    try:
        with open("directory.txt", "r") as file: root_dir = file.read()
        tickets = [[], [], []]
        for cycle, t_type in enumerate(TYPE):
            clean = []
            with open(f"{root_dir}/Overnight {t_type} Report.csv") as f: raw = list(reader(f))
            for index, row in enumerate(raw):  # Removes email headers, adds the index to the subject to avoid blank subjects, and skips the table headers
                if row[0] != "number": clean.append([row[0], sub(r'^(fw:|re:|fwd:)\s*', '', (row[1].lower()))])
            for x in clean:
                if x[1] == '': x[1] = "_no short description" + str(randint(0, 999))
            for x in clean: tickets[cycle].append(x)
        for x in range(3): tickets[x].sort(key=lambda rows: row[1])  # Sorts alphabetically by short description
    except (FileNotFoundError, IndexError):
        new_folder()
    return tickets

def new_folder(success=False):
    while not success:
        root_dir = str(fd.askdirectory())
        if root_dir == "": exit_app()
        for file in TYPE:
            try:
                with open(f"{root_dir}/Overnight {file} Report.csv") as f: raw = list(reader(f))
                print(raw[1])
                success = True
            except (FileNotFoundError, IndexError):
                mb.showerror(title="error!", message=f"Overnight {file} Report.csv is not present in this folder, or has become corrupted!")
                success = False
                break

    with open("directory.txt", "w") as file: file.write(root_dir)
    task_sort()


def exit_app():
    for thread in threading.enumerate():
        if thread.daemon: continue
        try: thread.join()
        except RuntimeError as e: print(f"Error while joining thread {thread}: {e}")
    root.destroy(); root.quit(); sys.exit()
