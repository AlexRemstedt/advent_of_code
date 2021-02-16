"""
	Doc Info:
		Author: Alex Remstedt	(https://github.com/AlexRemstedt)
		Github repo: (https://github.com/AlexRemstedt/advent_of_code)

	To do:
		TODO: passport Class
		TODO: __docs__ for list_fixer()
"""

# === Input ===
batch_file = [
	'ecl:gry pid:860033327 eyr:2020 hcl:#fffffd',
	'byr:1937 iyr:2017 cid:147 hgt:183cm',
	'',
	'iyr:2013 ecl:amb cid:350 eyr:2023 pid:028048884',
	'hcl:#cfa07d byr:1929',
	'',
	'hcl:#ae17e1 iyr:2013',
	'eyr:2024',
	'ecl:brn pid:760753108 byr:1931',
	'hgt:179cm',
	'',
	'hcl:#cfa07d eyr:2025 pid:166559648',
	'iyr:2011 ecl:brn hgt:59in'
]


# === List fixing functions ===
def list_fixer(broken_list):
	"""

	:param broken_list: a list consisting of string-parts broken up by empty strings.
	:return: a list with only full strings.
	"""
	fixed_list = []  # Empty list which shall be returned
	indices = break_finder(broken_list)
	for cluster in range(len(indices) - 1):
		# For loop variables
		broken_line = ''  # Empty string

		# For loop which looks at the lines within the clusters.
		for line in range(indices[cluster] + 1, indices[cluster + 1]):
			broken_line += broken_list[line] + ' '  # Adds broken_line-part to broken_line

		fixed_list.append(broken_line)  # append string (now full) to fixed list.
	return fixed_list


def break_finder(broken_list):
	"""
	break_finder takes a broken list an
	:param broken_list: a list which contains strings, seperated by ''.
	:return breaks: list with proper string, seperated by comma's
	"""
	# Function variables
	broken_lines = [-1, len(broken_list)]  # List with the indices of all the breakpoints, index -1 is the first breakline.

	# Finds index of where broken list is broken and appends index to broken_lines
	for idx, line in enumerate(broken_list):
		if line == '':
			broken_lines.append(idx)

	broken_lines.sort()  # Sorts the indexes
	return broken_lines


