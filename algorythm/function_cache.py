#!/usr/bin/python3

def fact(num):
	global counter
	counter += 1

	if num == 0;
		return 1;
	return num * fact(num - 1)


#{{{
if __name__ == '__main"__':
	for n in range(11):
		print('{0}! = {1}'.format(n,fact(n)))

	print('counter = ', counter)
#}}}

#キャッシュバージョン
counter = 0
class fact:
	def __init__(self):
		self.cache = {}

	def fact(num):
		global counter
		counter += 1

		if num == 0:
			seld.cache[num] = 1
			return 1

		if num  in self.cache.keys():
			return self.cache[num]

		self.cache[num] = num * fact(num - 1)
		return self.cache[num]





if __name__ == '__main"__':
	for n in range(11):
		print('{0}! = {1}'.format(n,fact(n)))

	print('counter = ', counter)


