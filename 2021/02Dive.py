""" Day 2 of advent of code.

What do you get if you multiply your final horizontal position by your final depth?
"""

with open('./inputs/2_Dive', 'r') as raw_inputs:
    movements = [line for line in raw_inputs]

    direction = [movement[0] for movement in movements]
    range_ = [int(movement[-2]) for movement in movements]

    horizontal = 0  
    aim = 0  
    depth = 0
    for r, d in zip(range_, direction):
        if d  == 'f':
            horizontal += r
            depth += r * aim
        elif d  == 'd':
            aim += r
        else:
            aim -= r
    print(horizontal * depth)

