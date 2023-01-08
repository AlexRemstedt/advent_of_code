"""Day 3: Rucksack Reorginazation."""
import sys


def main(path):
    ans = 0
    for line in open(path):
        x = line.strip()
        y, z = x[:len(x)//2], x[len(x)//2:]
        for c in y:
            if c in z:
                if 'a' <= c <= 'z':
                    ans += ord(c) - ord('a') + 1
                else:
                    ans += ord(c) - ord('A') + 1 + 26
                break
    print(ans)


if __name__ == "__main__":
    input_file = sys.argv[1] if len(sys.argv) > 1 else '03.x'
    main(input_file)
