from libraries import *

for x in range(1, 4):
    for y in range(1, 7):
        button.append(ButtonArray(x, y))
        radio.append(RadioArray(y))
        entry.append(EntryArray(y))
lists = Texties()
header = Header()
leaver = Leavers()
goer = Goer()



mainloop()