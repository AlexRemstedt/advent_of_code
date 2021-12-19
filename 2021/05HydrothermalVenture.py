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

# make grid_map
class GridMap:
    """Contain GridMap for lines."""

    def __init__(self, size):
        self.grid = np.array(shape=size)

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


def main():
    grid_map = np.zeros(shape=(max_,max_))

if __name__ == "__main__":
    main()

