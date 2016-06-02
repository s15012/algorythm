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

    draw = 1
    win = 2
    lose = 3

    judge = 0

    if user == gu and computer == gu:
        judge = draw
    elif user == gu and computer == tyoki:
        judge = win
    elif user == gu and computer == pa:
        judge = lose
    elif user == tyoki and computer == gu:
        judge = lose
    elif user == tyoki and computer == tyoki:
        judge = draw
    elif user == tyoki and computer == pa:
        judge = win
    elif judge == pa and computer == gu:
        judge = win
    elif judge == pa and computer == tyoki:
        judge = lose
    elif judge == pa and computer == pa:
        judge = draw

    if judge == draw:
        print("あいこ")
    elif judge == win:
        print("勝ち")
    elif judge == lose:
        print("負け")

end = time.time()
print("経過時間:", (end-start))

