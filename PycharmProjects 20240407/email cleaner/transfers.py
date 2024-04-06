from icecream import ic
import pyperclip as py


def transfer_clean(orig):
    top = py.paste()[:py.paste().find(orig)]
    bottom = (py.paste()[py.paste().find(orig):]).split("\n")
    top += f"{bottom[0]}\n{bottom[1]}\n"
    for line in bottom[2:10]: top += line * line.startswith("Contact type: ")
    py.copy(top)

oed = "************ Original Enquiry Details ************"
if oed in py.paste(): transfer_clean(oed)