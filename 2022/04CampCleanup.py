"""Day 4: Camp Cleanup."""
import sys


def range_maker(keys):
    r = list(map(int, keys.split('-')))
    return list(range(r[0], 1 + r[1]))


def part_1(path):
    cases = 0
    for line in open(path):
        elfs = line.strip().split(',')
        elfs = list(sorted([range_maker(elf)
                    for elf in elfs], key=len, reverse=True))
        if elfs[0][0] <= elfs[1][0] and elfs[0][-1] >= elfs[1][-1]:
            cases += 1
            # elfs[1] fully inside elfs[0]
        # elif elfs[0][0] <= elfs[1][0] and elfs[0][-1] >= elfs[1][0]:
        #     print(f'starts later but inside, case {case}')
    print(cases)
    return 0


def part_2(path):
    cases = 0
    for line in open(path):
        elfs = line.strip().split(',')
        elfs = list(sorted([range_maker(elf)
                    for elf in elfs], key=len, reverse=True))
        if elfs[0][0] <= elfs[1][0] and elfs[0][-1] >= elfs[1][-1]:
            cases += 1
        elif elfs[0][0] <= elfs[1][0] and elfs[0][-1] >= elfs[1][0]:
            cases += 1
        elif elfs[0][0] <= elfs[1][-1] and elfs[0][-1] >= elfs[1][-1]:
            cases += 1
    print(cases)
    return 0


if __name__ == "__main__":
    input_file = sys.argv[1] if len(sys.argv) > 1 else '04.x'
    part_1(input_file)
    part_2(input_file)
