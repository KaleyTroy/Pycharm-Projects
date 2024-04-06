from vars import *
import webbrowser as link
import pyperclip as cb


def update_name(event):
    for x in range(6):
        if x < radio_var.get(): print(name_space[x].get()); name_label[x] = name_space[x].get()
def suspend():
    for x in range(6):
        for y in range(3): tix[y][x].config(state="normal")
        name_space[x].config(state="normal"); name_space[x].delete(0, END); name_space[x].insert(END, name_label[x])
        if x >= radio_var.get():
            for y in range(3): tix[y][x].config(state="disabled")
            name_space[x].delete(0, END); name_space[x].insert(END, "none"); name_space[x].config(state="disabled")
def button_value(tm_rank, ticket_type):
    list_position_2 = int(len(tickets[ticket_type]) * ((tm_rank + 1) * radio_var.get()**-1))
    list_position_1 = int(len(tickets[ticket_type]) * (tm_rank * radio_var.get()**-1))
    text.delete(1.0, END); text.insert(1.0, tickets[ticket_type][list_position_1: list_position_2])
    heading.delete(0, END); heading.insert(0, f"{name_label[tm_rank]}'s {TYPE[ticket_type]}s | {the_day}")
    text.insert(1.0, f"{text.get('1.0', 'end-1c').count(',')} of {len(tickets[ticket_type])} tickets selected \n")

for x in range(6):
    ims.append(Button(text="IMS", border=3, font=font_l, command=lambda i=x: button_value(i, 0))); ims[x].grid(row=x, column=1, padx=5, pady=5)
    inc.append(Button(text="INC", border=3, font=font_l, command=lambda i=x: button_value(i, 1))); inc[x].grid(row=x, column=2, padx=5, pady=5)
    tas.append(Button(text="TAS", border=3, font=font_l, command=lambda i=x: button_value(i, 2))); tas[x].grid(row=x, column=3, padx=5, pady=5)
    radio_var_var = x + 1; radio.append(Radiobutton(value=radio_var_var, variable=radio_var, font=font_l, command=suspend)); radio[x].grid(row=x, column=4)
    name_label.append(f"Team Member {x + 1}")
    name_space.append(Entry(font=font_l, border=3, width=14)); name_space[x].grid(row=x, column=5)
    name_space[x].bind("<KeyRelease>", update_name); name_space[x].bind('<FocusIn>', lambda event: event.widget.select_range(0, END))

name_space[0].focus(); name_space[0].tkraise()
for i in range(1, 6): name_space[i].tkraise()

tix = [ims, inc, tas]
text = Text(width=20, height=14, font=font_s); text.grid(row=0, column=6, rowspan=5, padx=20, pady=20)
copy_text = Button(text="Copy Tickets", font=font_s, command=lambda: cb.copy(text.get("1.0", "end-1c"))); copy_text.grid(column=6, row=5)
heading = Entry(width=30, font=font_l); heading.grid(row=7, column=1, columnspan=5, pady=20)
copy_header = Button(text="Copy Header", font=font_s, command=lambda: cb.copy(heading.get())); copy_header.grid(column=6, row=7)

choose_folder = Button(font=font_s, text="Choose Folder", command=file_sort); choose_folder.grid(row=8, column=1, columnspan=6, sticky="w")
open_ims_list = Button(width=8, font=font_s, text="IMS List", command=lambda: link.open_new_tab(URL[0])); open_ims_list.grid(row=8, column=1, pady=20, padx=220, columnspan=6, sticky="w")
open_inc_list = Button(width=8, font=font_s, text="INC List", command=lambda: link.open_new_tab(URL[1])); open_inc_list.grid(row=8, column=1, pady=20, padx=20, columnspan=6)
open_tas_list = Button(width=8, font=font_s, text="TAS List", command=lambda: link.open_new_tab(URL[2])); open_tas_list.grid(row=8, column=1, pady=20, padx=220, columnspan=6, sticky="e")
close_button = Button(width=8, font=font_s, text="Close", command=lambda: root.destroy()); close_button.grid(row=8, column=1, columnspan=6, sticky="e")



suspend()
mainloop()
