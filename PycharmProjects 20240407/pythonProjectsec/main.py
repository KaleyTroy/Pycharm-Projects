with ("taxes.csv", "a") as file:
    new_entry = ""
    for x in ("Date", "Purchase", "Category", "Ammount"):
        new_entry += f"{input(x)},"

