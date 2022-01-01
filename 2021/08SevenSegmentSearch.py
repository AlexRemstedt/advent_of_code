"""Day 8: Seven Segment Search.

 a
b c
 d
e f
 g
"""


def get_input(path_to_file='./inputs/8_SevenSegmentSearch'):
    with open(path_to_file, 'r') as f:
        raw = f.readlines()
    raw = [line.split('|')[1].strip() for line in raw]
    raw = [words.split() for words in raw]
    return raw


def part1():
    lines = get_input()

    ez_digits = [2, 4, 3, 7]
    count = 0
    for digits in lines: 
        for digit in digits:
            if len(digit) in ez_digits:
                count += 1
    return count


if __name__ == "__main__":
    print(part1()) 


