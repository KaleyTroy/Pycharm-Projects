from file import *


def top_menu(b, a="coffee,levels,power".split(","), d=True):
    for b in range(len(a)):
        print(str(b) + ": " + str(a[b]))
    while d:
        c = input("?")
        if c.isalpha():
            for b in a:
                if c == a:
                    return c
        if c.isnumeric():
            c = int(c)
            if 0 <= c <= 4:
                return a[c]


def coffee(b, a="espresso,latte,cappuccino".split(",")):
    c = top_menu(b, a)


def levels(a):
    for key, value in a.items():
        print(key, value)


def power(a):
    print(a.items)


selection = top_menu(0)
eval(selection)(selection)
