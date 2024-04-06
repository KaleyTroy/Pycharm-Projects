from stringy import *
from headers import *
from transfers import *
from sett import *
from listcheck import *
from snowextractor import *

def heads():
    headers()


def clean():
    _ = "************ Original Enquiry Details ************"
    if _ in py.paste(): transfer_clean(_)
    cleaner()

def sett():
    setters()

def lists():
    list_check()

def snowextract():
    snow_extractor()


keyboard.add_hotkey("ctrl+alt+v", heads)
keyboard.add_hotkey("ctrl+alt+c", clean)
keyboard.add_hotkey("ctrl+alt+x", sett)
keyboard.add_hotkey("ctrl+alt+f", lists)
keyboard.add_hotkey("ctrl+alt+d", snowextract)
keyboard.wait("esc")