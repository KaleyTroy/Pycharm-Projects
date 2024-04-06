import keyboard
import pyperclip


def headers():
    email_text = pyperclip.paste()

    if not email_text:
        print("Clipboard is empty.")
        return

    lines = email_text.strip().split("\n")
    formatted_lines = []

    while lines:
        field = lines.pop(0)
        if len(field) > 2:
            if lines:
                value = lines.pop(0)
            else:
                value = "blank"
            formatted_lines.append(f"{field[:-1]}: {value}")

    pyperclip.copy("\n".join(formatted_lines))
    print(pyperclip.paste())
    for key in ("ctrl", "alt", "v"): keyboard.release(key)


# headers()