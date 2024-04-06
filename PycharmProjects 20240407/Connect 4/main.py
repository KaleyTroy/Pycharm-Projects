new = '''
 _________ _________ _________ _________ _________ _________ _________
|         |         |         |         |         |         |         |
|         |         |         |         |         |         |         |
|         |         |         |         |         |         |         |
|_________|_________|_________|_________|_________|_________|_________|
|         |         |         |         |         |         |         |
|         |         |         |         |         |         |         |
|         |         |         |         |         |         |         |
|_________|_________|_________|_________|_________|_________|_________|
|         |         |         |         |         |         |         |
|         |         |         |         |         |         |         |
|         |         |         |         |         |         |         |
|_________|_________|_________|_________|_________|_________|_________|
|         |         |         |         |         |         |         |
|         |         |         |         |         |         |         |
|         |         |         |         |         |         |         |
|_________|_________|_________|_________|_________|_________|_________|
|         |         |         |         |         |         |         |
|         |         |         |         |         |         |         |
|         |         |         |         |         |         |         |
|_________|_________|_________|_________|_________|_________|_________|
|         |         |         |         |         |         |         |
|         |         |         |         |         |         |         |
|         |         |         |         |         |         |         |
|_________|_________|_________|_________|_________|_________|_________|
|    1    |    2    |    3    |    4    |    5    |    6    |    7    |
                                                                       '''


def checker(grid_, tile_):
    line = 0
    x = grid_[tile_]
    q = [1, 6, 7, 8]

    for m in q:
        for n in range(tile_ - 3 * m, tile_ + 3 * m + 1, m):
            if 0 <= n <= 41:
                y = grid_[n]
                if x != y or y % 7 == 0:
                    line = 0
                else:
                    line += x
            if line == 4 * x:
                return "win"


column = ""
while column != "yes":
    board = list(new)
    player = False
    p = 2 * (float(player) - 0.5)
    square = [5, 5, 5, 5, 5, 5, 5]
    column = ""
    turn = -2
    print("".join(board))
    lup = 0
    grid = (list(str(10 ** 99)))[1:43]
    while not lup:
        column = input(f"Player {str(player + 1)}. Choose a column.").lower()

        if column.isnumeric():
            turn += 1
            column = int(column) - 1
            tile = square[column] * 7 + column
            grid[tile] = p

            a = (player * 72) + 147 + (square[column] * 288) + (column * 10)
            b = int(a + 72 * -p)
            board[a: a + 5] = list("\\\\_//")
            board[b: b + 5] = list("// \\\\")
            square[column] -= 1
            if turn:
                player = not player
                p = 2 * (float(player) - 0.5)
            print("".join(board))
            lup = checker(grid, tile)
    player = not player
    column = input(f"Player {str(player + 1)} Wins! Would you like to play again?").lower()

column = input("Thanks for playing :)")
