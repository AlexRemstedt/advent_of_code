#./venv/bin/python
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


def part2():
    #  d
    # e a
    #  f
    # g b
    #  c
    names = ['abcdeg', 'ab', 'acdfg', 'abcdf', 'abef', 'bcdef', 'bcdefg', 'abd',
            'abcdefg', 'abcdef']
    lines = get_input()
    count = 0
    for digits in lines: 
        print(digits)
        num = ''
        for digit in digits:
            sorted_dig = ''.join(sorted(digit))
            if len(sorted_dig) == 4:
                num += '4'
            elif len(sorted_dig) == 3:
                num += '7'
            elif len(sorted_dig) == 2:
                num += '1'
            elif len(sorted_dig) == 7:
                num += '8'
            elif sorted_dig in names:
                num += str(names.index(sorted_dig))
        print(num)
        count += int(num)
    return count


if __name__ == "__main__":
    print(part1()) 
    print(part2())


