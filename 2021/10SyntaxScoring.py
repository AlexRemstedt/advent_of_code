"""Day 10: Syntax Scoring."""

import sys
import numpy as np
from collections import deque


def part1(path: str):
    """What is the total syntax error score for those errors?"""
    nav_system = [line.strip() for line in open(path, 'r')]

    ans = 0
    chunks = []
    SCORES = []

    endings = {']': 57, '}': 1197, ')': 3, '>': 25137}
    beginnings = {'[': 2, '{': 3, '(': 1, '<': 4}
    for nr, line in enumerate(nav_system):
        line_is_good = True
        lefty = deque()
        for character in line.strip():
            if character in beginnings:
                lefty.append(character)
            elif character in endings:
                idx = list(endings).index(character)
                if lefty[-1] != list(beginnings)[idx]:
                    ans += list(endings.values())[idx]
                    line_is_good = False
                    break
                else: 
                    lefty.pop()
        if line_is_good:
            score = 0
            for character in reversed(lefty):
                score = score * 5 + beginnings[character]
            SCORES.append(score)

    print(ans)
    SCORES.sort()
    print(SCORES[len(SCORES)//2])

                
def main():
    input_file = sys.argv[1] if len(sys.argv) > 1 else '10.in'
    part1(input_file)


if __name__ == "__main__":
    main()


