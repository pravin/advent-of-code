#!/usr/bin/env python3

class Day01:
	_input = []
	def __init__(self):
		with open('input.txt') as fp:
			for line in fp:
				self._input.append(int(line.strip()))

	def puzzle1(self):
		return sum(self._input)

	def puzzle2(self):
		result = 0
		result_set = set([result])
		pos = 0
		length = len(self._input)

		while True:
			result += self._input[pos]
			if result in result_set:
				return result
			else:
				result_set.add(result)

			pos += 1
			if pos >= length:
				pos = 0


if __name__ == '__main__':
	d = Day01()
	#print(d.puzzle1())
	print(d.puzzle2())