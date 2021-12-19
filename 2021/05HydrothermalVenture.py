"""Day 5: Hydrothermal Venture."""

import numpy as np

def data_man():
    """Get data from inputfile."""
    # Main script
    with open('./inputs/5_HydrothermalVenture', 'r') as f:
        raw = [l for l in f]
    lines = []
    for coord_pair in raw:
        lines.append(coord_pair.split())

    # make data nice to work with
    for coord_pair in lines:
        del coord_pair[1]
        for n, coord in enumerate(coord_pair):
            coord_pair[n] = coord.split(',')
            for m, val in enumerate(coord_pair[n]):
                coord_pair[n][m] = int(val)
    return lines

    

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

    def draw_vertical(self, a, b):
        """Draw vertical lines in the grid."""
        if a[0] != b[0]:  # checks whether y is equal
            pass
        for x_coord in range(a[1], b[1])
            self.grid[a[0]][x] += 1
        return "Line drawn"

    def draw_horizontal(self, a, b):
        """Draw horizontal lines in the grid."""
        if a[1] != b[1]:  # checks whether y is equal
            pass
        for x_coord in range(a[0], b[0])
            self.grid[x][a[1]] += 1
        return "Line drawn"



def main():
    grid_map = GridMap.from_lines(lines)

if __name__ == "__main__":
    main()

