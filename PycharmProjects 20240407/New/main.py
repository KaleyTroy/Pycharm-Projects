from random import *

new = '''
                                                                       '''
a = "  2 of  ,  3 of  ,  4 of  ,  5 of  ,  6 of  ,  7 of  ,  8 of  ,  9 of  , 10 of  ,Jack of ,Queen of,King of , Ace of ".split(",") * 16
b = " Hearts ,Diamonds, Clubs  ,  Spades".split(",") * 4
for n in range(0, 16):
    for i in range(13 * n, 13 * n + 13):
        a[i] += b[n]
shuffle(a)
for i in a:
    print(i)

board = list(new)
print("".join(board))
grid = list(str(10 ** 99))[1:50]

t = 145
for i in range(0, 49):
    grid[i] = 73 + 10 * i
    if i % 7 == 0:
        grid[i] += 288
    board[grid[i]: grid[i] + 1] = a[i][0: 8]
    h = input("".join(board))
print("".join(board))

# c = col * 10 + row * 288 + z


# board[145: 152] = a[0][0: 7]
# board[218: 225] = a[0][8:15]
# print("".join(board))
# # board[c + 72: c + 77] =
