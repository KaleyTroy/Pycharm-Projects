import pandas

phonetic = """Alpha
Bravo
Charlie
Delta
Echo
Foxtrot
Golf
Hotel
India
Juliet
Kilo
Lima
Mike
November
Oscar
Papa
Quebec
Romeo
Siera
Tango
Uniform
Victor
Whiskey
X-ray
Yankee
Zulu""".split("\n")

phone_tool = {n[0]: n for n in phonetic}
letter = [n[0] for n in phonetic]
dick = {"ass": letter, "butt": phonetic}
print(dick)
pandas.DataFrame(dick).to_csv("gape.csv")
# gape.to_csv("gape.csv")

#
#
# while True:
#     piss = input("?").upper()
#     shit = [phone_tool[n] for n in piss]
#     print(shit)
#
