"""
	Doc Info:
		Author: Alex Remstedt (https://github.com/AlexRemstedt)		\n
		Github repo: (https://github.com/AlexRemstedt/advent_of_code)
"""

# === Variables ===
valid_passports = 0

# === Input ===
with open('input_files/day_4_input', 'r') as batch:
	batch_file = list(map(str, batch.read().splitlines()))
	pass


# === Passport Class ===
class Passport(object):
	eyecolors = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
	haircolors = '# 1 2 3 4 5 6 7 8 9 0 a b c d e f'.split()

	def __init__(self, birth_year, issue_year, expiration_year, height, hair_color, eye_color, passport_id, country_id):
		self.birthYear = birth_year
		self.issueYear = issue_year
		self.expirationYear = expiration_year
		self.height = height
		self.hairColor = hair_color
		self.eyeColor = eye_color
		self.passportId = passport_id
		self.countryId = country_id

	def is_valid(self):
		"""
		validate passport

		:return:
		"""
		if self.passportId and self.height and self.hairColor and self.issueYear and self.eyeColor and self.birthYear \
			and self.expirationYear:
			if len(self.hairColor) == 7:
				ls = [u for u in self.hairColor if u in self.haircolors]
				if len(ls) == 7:
					if 1920 <= int(self.birthYear) <= 2002 and 2010 <= int(self.issueYear) <= 2020 <= int(self.expirationYear) <= 2030:
						if self.eyeColor in self.eyecolors and len(self.passportId) == 9:
							if type(self.height) == str and self.height[-2:] == 'cm' and 150 <= int(self.height[:-2]) <= 193:
								return True
							elif type(self.height) == str and self.height[-2:] == 'in' and 59 <= int(self.height[:-2]) <= 76:
								return True


	@classmethod
	def from_string(cls, string):
		"""
		Alternative builder

		:param string: passport input in string format
		:type string: str
		:return: returns class for passport
		"""
		keys = string.split(' ')
		byr = False
		iyr = False
		eyr = False
		hgt = False
		hcl = False
		ecl = False
		pid = False
		cid = False
		for key in keys:
			if key[:3] == 'byr':
				byr = key[4:]
			elif key[:3] == 'iyr':
				iyr = key[4:]
			elif key[:3] == 'eyr':
				eyr = key[4:]
			elif key[:3] == 'hgt':
				hgt = key[4:]
			elif key[:3] == 'hcl':
				hcl = key[4:]
			elif key[:3] == 'ecl':
				ecl = key[4:]
			elif key[:3] == 'pid':
				pid = key[4:]
			elif key[:3] == 'cid':
				cid = key[4:]
		return cls(byr, iyr, eyr, hgt, hcl, ecl, pid, cid)


# === List fixing functions ===
def list_fixer(broken_list):
	"""
	list_fixer fixes the broken_list.
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


# === Dictionary ===
passports = {}
for i in range(len(list_fixer(batch_file))):
	passports.update({i: Passport.from_string(list_fixer(batch_file)[i])})
	x = (passports[i].is_valid())
	if x:
		valid_passports += 1

print(valid_passports)
