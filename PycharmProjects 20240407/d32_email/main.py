import keyboard
import pyperclip


def reformat_email():
    email_text = pyperclip.paste()
    if not email_text:
        print("Clipboard is empty.")
        return

    lines = email_text.strip().split("\n")
    formatted_lines = []

    while lines:
        field = lines.pop(0)
        print(field)
        if len(field) > 2:
            if lines:
                value = lines.pop(0)
                print(value)
            else:
                value = "blank"
                print(value)
            formatted_lines.append(f"{field}: {value}")

    formatted_email = "\n".join(formatted_lines)
    keyboard.write(formatted_email)
    keyboard.release("ctrl")
    keyboard.release("alt")
    keyboard.release("v")

def clean_email():
    email_text = pyperclip.paste()
    lines = email_text.strip().split("\n")
    print(lines)
    keyboard.release("ctrl")
    keyboard.release("alt")
    keyboard.release("e")


keyboard.add_hotkey("ctrl+alt+v", reformat_email)
keyboard.add_hotkey("ctrl+alt+e", clean_email)
keyboard.wait("esc")
