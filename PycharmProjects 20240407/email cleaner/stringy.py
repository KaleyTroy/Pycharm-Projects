from re import *
import keyboard
import pyperclip as py

strings = (
    ("<mailto:", ">", ""),
    ("You don't often get email", "Learn why this is important", ""),
    ("<https://protect", ">", ""),
    ("This email is confidential", "delete the document.", ""),
    ("[cid:", "]", ""),
    ("⚠ EXTE", "e. ⚠", ""),
    ("Caution: This", "unsure of this email.", ""),
    ("<http", ">", ""),
    ("[http", "]", ""),
    ("[cid", "]", ""),
    ("[email+", "]", ""),
    ("[cid", "]", ""),
    ("This email is confidential", "legally privileged information.", ""),
    ("If you are not the intended", "information contained in it.", ""),
    ("If you have received", "email and delete the document", ""),
    ("Please consider the environme", "nt before printing this e-mail.", ""),
    ("Information in this message is confidential", "message from your computer.", ""),
    ("This system may be monitored or recorded ", "website for details.", ""),
    ("This is an automated", "end", ""),
    ("************ Ori", "ils ************", "=== Original Enquiry Details ==="),
    ("[image", "]", ""),
    ("https://protect.checkpoint.com", " ", ""),
    ("This message and its attac", "ase request a hard-copy version.", ""),
    ("<tel:", ">", ""),
    ("I respectfully acknow", " for our future generations.", ""),
    ("</care/attachment", ">", ""),
    ("Caution: This email", "know the content is safe.", ""),
    ("This email message", "or any attached or linked files.", ""),
    ("__start__", "end", ""),
    ("__start__", "end", ""),

)


def cleaner():
    mail = py.paste()
    for start, end, new in strings:
        mail = sub(escape(start) + "(.*?)" + escape(end), new, mail)

    print(mail)
    py.copy(mail)
    for key in ("ctrl", "alt", "c"): keyboard.release(key)

# cleaner()