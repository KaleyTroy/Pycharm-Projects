import keyboard
import pyperclip

def setters():
    email_text = pyperclip.paste()

    if not email_text:
        print("Clipboard is empty.")
        return

    lines1 = "Sent email:\n"
    lines2 = email_text
    lines3 = "\n\nKind Regards\nKohdi Mahboub (They/Them)\nService Desk Officer, Technology Services"
    lines4 = lines1 + lines2 + lines3
    pyperclip.copy(lines4)
    print(pyperclip.paste())

    for key in ("ctrl", "alt", "x"): keyboard.release(key)

