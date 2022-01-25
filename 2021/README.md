# Advent of Code - 2021

## toc

## Day 8

I used code from [this video](https://youtu.be/DhQPrF-LBoE).

```py
def part1(path_to_file='./inputs/8_SevenSegmentSearch'):
    ans = 0
    for line in open(path_to_file, 'r'):
        before, after = line.split('|')
        before = before.split()
        after = after.split()
        # Store lengths and words.
        by_len = defaultdict(list)
        for word in before:
            by_len[len(word)].append(word)
        for word in after:
            # If word is unique, then there is only 1 of them.
            if len(by_len[len(word)]) == 1: 
                ans += 1
    print(ans)
```

## Day 9

finally [looked up](https://docs.python.org/3.8/libray/functions.html#map) what
`map()` does. 

Needed a bit of help used code from [this
guy](https://zonito.medium.com/smoke-basin-day-9-advent-of-code-2021-python-solution-54c8d3da58a7).

## Day 10

some are incomplete
others are corrupt.
corrupt: closes with the wrong character

Problem: now only looks @ first beginning
Have to find a way to look between linked chars.
Idea: find()

