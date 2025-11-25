i = []
while True:
    try:
        line = input()
        i.append(line)
    except EOFError:
        break

total_area = 0
ribbon_length = 0

for box in i:
    if "x" not in box:
        continue
    dims = sorted(list(map(int, box.split("x"))))
    area = 3 * dims[0] * dims[1] + 2 * dims[1] * dims[2] + 2 * dims[0] * dims[2] 
    ribbon_length += 2 * dims[0] + 2 * dims[1] + dims[0] * dims[1] * dims[2]
    total_area += area

print(total_area)
print(ribbon_length)
