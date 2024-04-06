from vars import *
def tm_name(event):
    for x in range(6):
        if x < radio_var.get(): name_var[x] = name_space[x].get()
    heading.delete(0, END)

def tm_radio():
    tickets = task_sort(); global tms; hop = 0
    # Disables the Buttons and Entries below the selected radio button
    for radio_row in range(6):
        for y in range(3): array[y][radio_row].config(state="normal")
        name_space[radio_row].config(state="normal"); name_space[radio_row].delete(0, END); name_space[radio_row].insert(END, name_var[radio_row])
        if radio_row >= radio_var.get():
            for y in range(3): array[y][radio_row].config(state="disabled")
            name_space[radio_row].delete(0, END); name_space[radio_row].insert(END, "none"); name_space[radio_row].config(state="disabled")
    # Divides all tickets between team members
    for tick_type in range(3):
        for x in range(len(tickets[tick_type])):
            rank = hop % radio_var.get(); tms[rank].append(tickets[tick_type].pop(0))
            try:
                if tickets[tick_type][0][1] != tms[rank][-1][1]: hop += 1
            except IndexError: heading.delete(0, END)
    #
def button_action(tm_rank, ticket_type):
    heading.delete(0, END); heading.insert(0, f"{name_var[tm_rank]}'s {TYPE[ticket_type]}s | {the_day}")
    text.delete(1.0, END); current = []
    tms[tm_rank][0] = [name_var[tm_rank], 0, 0, 0]
    for x in tms[tm_rank]:
        if x[0][:3] == TYP[ticket_type]: current.append(f"{x[0]},\n")
        for tipe in range(3): tms[tm_rank][0][tipe + 1] += x[0][:3] == TYP[tipe]
    for x in tms[tm_rank]: print(x)
    print("\n")
    for x in current: text.insert(1.0, x)

# Main array
for row in range(6):
    ims.append(Button(text="IMS", border=3, font=large, command=lambda j=row: button_action(j, 0))); ims[row].grid(row=row, column=1, padx=5, pady=5)
    inc.append(Button(text="INC", border=3, font=large, command=lambda k=row: button_action(k, 1))); inc[row].grid(row=row, column=2, padx=5, pady=5)
    tas.append(Button(text="TAS", border=3, font=large, command=lambda l=row: button_action(l, 2))); tas[row].grid(row=row, column=3, padx=5, pady=5)
    radio_var_var = row + 1; radio.append(Radiobutton(value=radio_var_var, variable=radio_var, font=large, command=tm_radio)); radio[row].grid(row=row, column=4)
    name_var.append(f"Team Member {row + 1}")
    name_space.append(Entry(font=large, border=3, width=14)); name_space[row].grid(row=row, column=5)
    name_space[row].bind("<KeyRelease>", tm_name); name_space[row].bind('<FocusIn>', lambda event: event.widget.select_range(0, END))
    tms.append([["", 0, 0, 0]])

# Additional widgets
name_space[0].focus(); name_space[0].tkraise()
for i in range(1, 6): name_space[i].tkraise()
array = [ims, inc, tas]
text = Text(width=20, height=14, font=small); text.grid(row=0, column=6, rowspan=5, padx=20, pady=20)
copy_text = Button(text="Copy Tickets", font=small, command=lambda: cb.copy(text.get("1.0", "end-1c"))); copy_text.grid(column=6, row=5)
heading = Entry(width=36, font=large); heading.grid(row=7, column=1, columnspan=5, pady=20)
copy_header = Button(text="Copy Header", font=small, command=lambda: cb.copy(heading.get())); copy_header.grid(column=6, row=7)
# Bottom buttons
choose_folder = Button(font=small, text="Choose Folder", command=new_folder); choose_folder.grid(row=8, column=1, columnspan=6, sticky="w")
open_ims_list = Button(width=8, font=small, text="IMS List", command=lambda: link.open_new_tab(URL[0])); open_ims_list.grid(row=8, column=1, pady=20, padx=220, columnspan=6, sticky="w")
open_inc_list = Button(width=8, font=small, text="INC List", command=lambda: link.open_new_tab(URL[1])); open_inc_list.grid(row=8, column=1, pady=20, padx=20, columnspan=6)
open_tas_list = Button(width=8, font=small, text="TAS List", command=lambda: link.open_new_tab(URL[2])); open_tas_list.grid(row=8, column=1, pady=20, padx=220, columnspan=6, sticky="e")
close_button = Button(width=8, font=small, text="Close", command=exit_app); close_button.grid(row=8, column=1, columnspan=6, sticky="e")  # The lower buttons

tm_radio()
mainloop()
