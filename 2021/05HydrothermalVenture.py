"""Day 5: Hydrothermal Venture."""

from typing import List
import numpy as np


def data_manipulation():
    """Get data from inputfile."""
    # Main script
    with open('./inputs/5_HydrothermalVenture', 'r') as f:
        raw = [l for l in f]
    lines = []
    for coord_pair in raw:
        lines.append(coord_pair.split())

    # Make data nice to work with
    for coord_pair in lines:
        del coord_pair[1]
        for n, coord in enumerate(coord_pair):
            coord_pair[n] = coord.split(',')
            for m, val in enumerate(coord_pair[n]):
                coord_pair[n][m] = int(val)
    return lines
    

# Make grid_map
class GridMap:
    """Contain GridMap for lines."""

    def __init__(self, size):
        self.grid = np.zeros(shape=size)

    @classmethod
    def from_lines(cls, lines):
        """Create GridMap instance from lines.

        Determine the correct size by looking for the longest line
        """
        max_ = 0
        for line in lines:
            for coord in line:
                for value in coord:
                    if value > max_:
                        max_ = value
        return cls(size=(max_, max_))


class Line:
    """Line object."""

    def __init__(self, point_1: List[float], point_2: List[float]):
        self.a = tuple(point_1)
        self.b = tuple(point_2)


def main():
    """Main function."""
    basic_lines = data_manipulation()
    lines = []
    for line in basic_lines:
        lines.append(Line(line[0], line[1]))
    print(lines)

if __name__ == "__main__":
    main()

