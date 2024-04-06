import pandas
piss = pandas.read_csv("gape.csv")
piss.drop(piss.filter(regex="Unname"), axis=1, inplace=True)
dick = {b.ass: b.butt for a, b in piss.iterrows()}

while True:
    print([dick[n] for n in input("?").upper()])
