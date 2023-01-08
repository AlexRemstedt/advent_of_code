"""Day 3: Rucksack Reorginazation."""
import sys


def score(c):
    if 'a' <= c <= 'z':
        return ord(c) - ord('a') + 1
    return ord(c) - ord('A') + 1 + 26


def part_1(path):
    ans = 0
    for line in open(path):
        x = line.strip()
        y, z = x[:len(x)//2], x[len(x)//2:]
        for c in y:
            if c in z:
                ans += score(c)
    print(ans)


def part_2(path):
    ans = 0
    x = [line for line in open(path)]
    i = 0
    while i < len(x):
        for c in x[i]:
            if c in x[i+1] and c in x[i + 2]:
                ans += score(c)
                break
        i += 3
    print(ans)


if __name__ == "__main__":
    input_file = sys.argv[1] if len(sys.argv) > 1 else '03.x'
    part_1(input_file)
    part_2(input_file)
