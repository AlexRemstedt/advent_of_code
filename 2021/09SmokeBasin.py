"""Day 9: Smoke Basin."""

import sys
from math import prod

def part1(input_file: str) -> int:
    """Find the low points."""
    # Create map.
    grid = []
    for line in open(input_file, 'r'):
        line = line.strip()
        grid.append(list(map(int, line)))

    def find_adj(i, j):
        adj = []
        if i + 1 < len(y_val_row):
            adj.append(y_val_row[i + 1])
        if i - 1 >= 0:
            adj.append(y_val_row[i - 1])
        if j + 1 < len(grid):
            adj.append(grid[j + 1][i])
        if j - 1 >= 0:
            adj.append(grid[j - 1][i])
        return adj

    out = 0
    for j, y_val_row in enumerate(grid):
        for i, x_val in enumerate(y_val_row):
            if x_val < min(find_adj(i, j)):
                out += 1 + x_val
    return out


def part2(input_file: str) -> int:
    """Find every basin.
 
    Every low point has a basin surrounding it.
    """
    grid = []
    for line in open(input_file):
        line = line.strip()
        grid.append(list(map(int, line)))

    def count_group(i, j):
        block = [-1, 9]
        j_block = list(range(0, len(grid)))
        i_block = list(range(0, len(grid[0])))
        if j not in j_block or i not in i_block or grid[j][i] in block:
            return
        grid[j][i] = -1
        groups[-1] += 1
        count_group(i + 1, j)
        count_group(i - 1, j)
        count_group(i, j + 1)
        count_group(i, j - 1)

    groups = []
    for j, line in enumerate(grid):
        for i, x in enumerate(line):
            groups.append(0)
            count_group(i, j)
    print(prod(sorted(groups, reverse=True)[:3]))


def main():
    input_file = sys.argv[1] if len(sys.argv) > 1 else '9.in'
    part1(input_file)
    part2(input_file)


if __name__ == "__main__":
    main()


