from random import *
import prettytable

table = prettytable.PrettyTable()
table.add_column("Pokemon Name", ["Bulbasaur", "Squirtle", "Charmander"])
table.add_column("TypeTypeType", ["Grass", "Water", "Fire"])
q = "lcr"
while True:
    r = randint(0, 2)
    table.align = q[r]
    r = randint(0, 2)
    table.align["TypeTypeType"] = q[r]
    print(table)
