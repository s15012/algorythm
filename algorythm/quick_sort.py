#!/usr/bin/python3
LIST_COUNT = 1000
LOOP_COUNT = 3000
MAX_NUM = 10000

def data_generate():
  import random
  return [random.randint(1, MAX_NUM) for _ in range(LIST_COUNT)]


def quick_sort(data):
  if len(data) <= 1:                    #データの長さが条件より小さい場合にデータを返す
    return data


  pivot = data[0]

  left = []                             #データの格納庫
  right = []

  for x in range(1, len(data)):         #データXがPivot以下の場合、データXのLeftにデータを追加。
    if data[x] <= pivot:
      left.append(data[x])
    else:
      right.append(data[x])             #条件以外の場合は右に追加

  left = quick_sort(left)
  right = quick_sort(right)

  return left + [pivot] + right



def quick_sort2(data):
  if len(data) <= 1:                    #データの長さが条件より小さい場合にデータを返す
    return data


  pivot = data[0]

  left = []                             #データの格納庫
  right = []

  for x in range(1, len(data)):         #データXがPivot以下の場合、データXのLeftにデータを追加。
    if data[x] <= pivot:
      left.append(data[x])
    else:
      right.append(data[x])             #条件以外の場合は右に追加

  left = quick_sort(left)
  right = quick_sort(right)

  return left + [pivot] + right








if __name__ == '__main__':
  import time
  import sys

  start = time.time()

  for _ in range(LOOP_COUNT):
    data = data_generate()
    quick_sort(data)
    [print('・。・', quick_sort(data), end='') if _ % 100 != 99 else print(int(_ / 100 + 1))]
    sys.stdout.flush()


  end = time.time()
  print()
  print('経過時間:', (end-start))
  print('平均時間:', ((end-start) / LOOP_COUNT))

