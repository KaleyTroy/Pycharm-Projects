import pandas
from collections import Counter
#
# bookywook = {
#     "penis": ['dick', 'cock', 'willy'],
#     "vagina": ['cunt', 'fanny', 'tuppy']
# }
#
# framez = pandas.DataFrame(bookywook)
# framez.to_csv("framez.csv")
# Primary Fur Color

project = pandas.read_csv("squirel.csv")
fur = project["Primary Fur Color"]
shit = dict(Counter(fur))
piss = {
    "primary fur color": ["Gray", "Black", "Cinnamon"],
    "number": [shit["Gray"], shit["Black"], shit["Cinnamon"]]
}
butt = pandas.DataFrame(piss)
butt.to_csv("furries.csv")
