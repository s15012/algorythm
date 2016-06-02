#! /usr/bin/python3

import time
import random

LOOP_COUNT = 1000000

start = time.time()

for _ in range(LOOP_COUNT):

    user = random.randint(1,4)
    computer = random.randint(1,4)

    gu = 1
    tyoki = 2
    pa = 3

    draw = 0
    win = 2
    lose = 1

    judge = (user - computer + 3) % 3

    if (judge == draw):
        print("あいこ")
    elif (judge == win):
        print("勝ち")
    elif (judge == lose):
        print("負け")

end = time.time()
print("経過時間:", (end-start))
