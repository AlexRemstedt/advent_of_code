import numpy as np

file3 = open('input_files/day_3_input', 'r')
forest = list(map(str, file3.read().splitlines()))  # map() makes it iterate
file3.close()


def char_finder(ls, dy, dx):
    char_count = 0
    x = 0
    for y in range(0, len(ls), dy):
        if ls[y][x] == '#':
            char_count += 1
        if x + dx >= len(ls[y]):
            x += dx - len(ls[y])
        else:
            x += dx
    return char_count


ans = 1
x_hop = [1, 3, 5, 7, 1]
y_hop = [1, 1, 1, 1, 2]
for n in range(0, 5):
    ans = ans * char_finder(forest, y_hop[n], x_hop[n])
print(ans)
