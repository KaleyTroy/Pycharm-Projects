SWITCH = 1
TOP = ["1 coffee", "2 levels", "3 power"]
COFFEES = ["1 espresso", "2 latte", "3 cappuccino"]
POWER = ["1 power off", "2 return"]
COINS = ["1 penny", "2 nickel", "3 dime", "4 quarter", "5 loonie", "6 twonie"]
WORTH = {"penny": 1, "nickel": 5, "dime": 10, "quarter": 25, "loonie": 100, "twonie": 200}
RESOURCES = {"water": 300, "milk": 200, "coffee": 100}
PROFIT = 0
MENU = {"espresso": {"ingredients": {"water": 50, "milk": 0, "coffee": 18}, "cost": 150},
        "latte": {"ingredients": {"water": 200, "milk": 150, "coffee": 24}, "cost": 250},
        "cappuccino": {"ingredients": {"water": 250, "milk": 100, "coffee": 24}, "cost": 300}}


def top_menu(x):
    for a in x:
        print(a)
    b = x[int(input("?")) - 1][2:]
    print(b)
    return b


def coffee():
    recipe = top_menu(COFFEES)
    for x in MENU[recipe]["ingredients"]:
        if RESOURCES[x] - MENU[recipe]["ingredients"][x] < 0:
            print(f"Sorry, I'm running low on {x}")
            return
        RESOURCES[x] -= MENU[recipe]["ingredients"][x]
    price = MENU[recipe]["cost"]
    while price > 0:
        print(f"please deposit ${price / 100}")
        price -= round(WORTH[top_menu(COINS)], 2)
    global PROFIT
    PROFIT += MENU[recipe]["cost"]
    return


def levels():
    for s, t in RESOURCES.items():
        print(s, t)
    global PROFIT
    print(f"${PROFIT / 100}")
    input("1 return")
    return


def power():
    if top_menu(POWER) == "power off":
        global SWITCH
        SWITCH = 0
    return


while SWITCH:
    step_1 = top_menu(TOP)
    step_2 = eval(step_1)()


print("Goodbye!")
