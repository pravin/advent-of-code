#!/usr/bin/env python3

class Day08:
	_input = []

	def __init__(self):
		with open('input.txt') as fp:
			self._input = fp.read().strip().split(' ')


	def puzzle1(self, str):
		num_child_nodes = int(str[0])
		num_meta_data = int(str[1])
		pos = 2 # Skip the first two elements
		result = 0
		for i in range(num_child_nodes):
			chars_consumed, sum_meta = self.puzzle1(str[pos:])
			pos += chars_consumed
			result += sum_meta

		for i in range(num_meta_data):
			result += int(str[pos+i])

		return pos + num_meta_data, result


if __name__ == '__main__':
	d = Day08()
	print(d.puzzle1(d._input))