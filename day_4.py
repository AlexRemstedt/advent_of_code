# Input
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


# Finds where every break is.
for idx, line in enumerate(batch_file):
	if line == '':
		passport_holder_spaces.append(idx)

passport_holder_spaces.append(len(batch_file))


# Functions
def passport_detail_string(break1, break2, array):
	"""
	Defines each passport_detail_string input.
	:type break1: int
	:type break2: int
	:type array: list
	"""
	info = ''
	for rule in range(break1, break2, 1):
		info += array[rule] + ' '
	return info




# Finds where every break is.
passport_places = [-1]

for idx, line in enumerate(batch_file):
	if line == '':
		passport_places.append(idx)

passport_places.append(len(batch_file))

for index in range(0, len(passport_places) - 1, 1):
	print(passport_detail_string(passport_places[index] + 1, passport_places[index + 1], batch_file))
