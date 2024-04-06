import keyboard
import pyperclip
import re
from icecream import *

def snow_extractor():
    grab = re.sub(r'\s*\n\s*\n\s*\n\s*', '\n=== ===\n', pyperclip.paste(), count=1)
    grab = re.sub(r'\s*\n\s*\n\s*\n\s*\n\s*', '\n\n', grab)
    grab = re.sub(r'\s*\n\s*\n\s*\n\s*', '\n\nNone\n\n', grab)
    grab = re.sub(r'\t', ' {tab} ', grab)
    grab = re.sub(r'\s*\n\s*\n\s*', '\n', grab).splitlines()[3:]

    for x, i in enumerate(grab):
        if i == "=== ===": columns = x; del grab[x];break

    tab_separated_list = []
    while grab:
        tab_separated_list.append(grab[:columns])
        grab = grab[columns:]

    tab_separated_list_string = '\n'.join(['\t'.join(map(str, row)) for row in tab_separated_list])
    print(tab_separated_list_string)
    pyperclip.copy(tab_separated_list_string)