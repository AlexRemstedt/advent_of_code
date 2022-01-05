"""Day 1.

How many measurements are larger than the previous measurment.

Notes: origineel zelf gemaakt; 
verbeterd met https://mathspp.com/blog/advent-of-code-sonar-sweep-analysis
"""


import sys
from itertools import tee


def pairwise(it):
    """Mock `itertools.pairwise` for python version below 3.10."""
    prev_, next_ = tee(it, 2)
    next(next_)
    yield from zip(prev_, next_)

input_ = sys.argv[1] if len(sys.argv) > 1 else '1.in'
# Task 1
with open(input_, 'r') as raw_inputs:
    # integer-ify 
    # use brackets for generator-expression
    depths = (int(line) for line in raw_inputs)

    # voor zip() neemt hij altijd de grootte van de kleinste
    count1 = sum(prev_ < next_ for prev_, next_ in pairwise(depths))
print(count1)


# Task 2 (Also generalised.)
window_size = 3
with open(input_, 'r') as raw_inputs:
    depths = (int(line) for line in raw_inputs)
    window = [next(depths) for _ in range(window_size)]
    count = 0
    for elem in depths:
        window.append(elem)
        if window[0] < window[-1]:
            count += 1
        window.pop(0)

    print(count)
