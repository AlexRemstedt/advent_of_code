# encoding: utf-8
# author: AlexRemstedt (https://github.com/AlexRemstedt)
"""
Find the highest ID using binary space partioning
[https://adventofcode.com/2020/day/5]
"""


def row_calc(string):
	"""
	calculate row number using binary space partitioning

	:param string: A piece of string with 'F' and 'B'
	:type string: str
	:return: Location of seat
	:rtype: int
	"""
	row = [0, 127]
	for x in string:
		if row[1] - row[0] == 1:
			if x == 'F':
				return row[0]
			elif x == 'B':
				return row[1]
		elif x == 'F':
			row[1] -= round((row[1] - row[0]) / 2)
		elif x == 'B':
			row[0] += round((row[1] - row[0]) / 2)


def col_calc(string):
	"""
	calculate column number using binary space partitioning

	:param string: A piece of string with 'R' and 'L'
	:type string: str
	:return: Location of seat
	:rtype: int
	"""
	col = [0, 7]
	for x in string:
		if col[1] - col[0] == 1:
			if x == 'R':
				return col[1]
			elif x == 'L':
				return col[0]
		elif x == 'R':
			col[0] += round((col[1] - col[0]) / 2)
		elif x == 'L':
			col[1] -= round((col[1] - col[0]) / 2)


def seat_id(string):
	"""
	Calculate seat ID based on position of seat.

	:param string: A piece of string with 'F' and 'B'
	:type string: str
	:return: seat id
	:rtype: int
	"""
	return row_calc(string) * 8 + col_calc(string)


# input
def main():
	x = []

	# open file
	with open('input_files/day_5_input', 'r') as batch:
		for line in batch:
			x.append(seat_id(line))
	print(max(x))


if __name__ == "__main__":
	main()