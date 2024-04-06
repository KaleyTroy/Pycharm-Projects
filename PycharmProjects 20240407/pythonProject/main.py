import random
from hangman_words import word_list
from hangman_art import stages
from geslet import geslet_allfalse

#      0     1      2      3
lif = [6, stages, True, input("Welcome to Hangman!")]
print(lif[1][lif[0]])


sol = [random.choice(word_list)]
#        0          1          2           3
sol = [sol[0], list(sol[0]), False, len(sol[0])]

if lif[3] == "cheat":
    print(sol[0])


ges = [""]
for n in range(sol[3]):
    ges[0] += "-"
print(ges[0])
  #      0          1           2           3           4
ges = [ges[0], list(ges[0]), False, geslet_allfalse, input("Please guess your first letter: ")]
for m in sol[1]:
    for n in ges[3]:
        if m == n:
            ges[3][n][0] = True
ges[4] = ges[4][0].lower()

# print(ges[3][ges[4]])
#
# while not sol[2] and lif[2]:
#     if ges[3][ges[4]]:
#         print("Looks like you've already guessed that one")
#         for n in ges[3]:
#             if ges[3][n]:
#                 lif[3] += n
#         print("Previous guesses: " + lif[3])
#         lif[3] = ""
#     else:
#         ges[3][ges[4]][1] = True
#
#
#
#         ges[4] = input("Please choose another letter: ")
#         if ges[4] == "":
#             lif[2] = False
#
# print("Game Over")
#
#
