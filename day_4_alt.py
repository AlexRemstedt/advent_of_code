file4 = open('input_files/day_4_input', 'r')
batch_file = list(map(str, file4.readlines()))
file4.close()

cool_store = []

for n in batch_file:
	x = n.split()
	if x:
		cool_store += x

fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']

cool_store.sort()
m = []
for var in fields:
	m.append(sum(var in s for s in cool_store))
print(min(m))
