# Advent of Code - 2021

## toc

## Day 8

I used code from [https://youtu.be/DhQPrF-LBoE](this video).

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
