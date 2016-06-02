#! /usr/bin/python3

import time
import random

LOOP_COUNT = 1000


start = time.time()

for _ in range(LOOP_COUNT):

    user = random.randint(1,4)
    computer = random.randint(1,4)

    gu = 1
    tyoki = 2
    pa = 3

    draw = 1
    win = 2
    lose = 3

    judge = ([ draw, win, lose],[ lose, draw, win],[win, lose, draw])

    if (judge[user - 1][computer - 1] == draw):
        print("あいこ\n")
    elif (judge[user - 1][computer - 1] == win):
        print("勝ち\n")
    elif (judge[user - 1][computer - 1] == lose):
        print("負け\n")

end = time.time()
print("経過時間:", (end - start))

