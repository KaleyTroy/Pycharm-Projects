from random import *
from art import *

board_art = list(board_)
deck_art = list(deck_)
deck = [new_deck(4)]
board = new_board()
spot = []
p = number_of_players()
plr = the_players(p)

for z in range(p):# picks and prints the player names and starting balances
    board_art[plr[0][0]: plr[0][1]] = plr[0][2]
    board_art[plr[0][3]: plr[0][4]] = plr[0][5]

board_art[191:198] = "Place  "
board_art[291:298] = "   Your"
board_art[391:398] = " Bets! "

print("".join(board_art))
for n in range(0, p):
    check = 0
    while not check:
        bet = input(f"{plr[n][0]}, place your bet! ")
        if bet.isnumeric():
            if float(bet) % 5 == 0:
                plr[n][2] = bet
                nb = str(plr[n][2])
                board_art[301 + n * 10: 302 + n * 10 + len(nb)] = "$" + nb
                check = 1
                print("".join(board_art))

board_art[191:198] = "       "
board_art[291:298] = "No more"
board_art[391:398] = " Bets! "

print("".join(board_art))
for n in range(0, plr):
    for m in range(4, 6):
        deck[1].insert(deck[0].pop(0))
        plr[n][m][1] = deck[1][0]
        spot = plr[n][4][0]
        b = next_spot(spot)
        c = top_card(plr)
        for a in range(0, 400, 100):
            board_art[b[4] + a: b[5] + a] = deck_art[c[4] + a:c[5] + a]
print("".join(board_art))


# for q in range(1, 21):
#     spot = q + 1 / 10
#     played = deck.pop(0)
#     b = next_spot(spot)
#     c = top_card(played)
#     for a in range(0, 400, 100):
#         board_art[b[3] + a: b[4] + a] = deck_art[c[3] + a:c[4] + a]
# print("".join(board_art))
