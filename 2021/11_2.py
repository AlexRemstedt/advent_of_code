"""Day 11: Dumbo Octopus."""

"""
5483143223
2745854711
5264556173
6141336146
6357385478
4167524645
2176841721
6882881134
4846848554
5283751526
"""

import sys
import numpy as np

class Octopus:
    """Hold energylevels."""

    def __init__(self, initial_energy_level):
        self.energy_level = initial_energy_level

    def get_boost(self):
        self.energy_level += 1

    @staticmethod
    def get_neighbours(x, y):
        """Get neighbours of octopus.

        [-1, -1] [0, -1] [1, -1]
        [-1, 0]  [x, y]  [1, 0]
        [-1, 1]  [0, 1]  [1, 1]
        """
        # find surrounding
        surrounders = [(-1, -1), (0, -1), (1, -1), (-1, 0), (1, 0), (-1, 1),
                       (0, 1), (1, 1)]
        neighbours = []
        for (x, y) in surrounders:
            new_x = center[1] + x
            new_y = center[1] + y
            if new_x in self.range_[0] and new_y in self.range_[1]
                neighbours.append((new_x, new_y))
                self.grid[new_y][new_x].get_boost()
        return neighbours


class OctopusGrid:
    """Hold octopus positions."""

    def __init__(self, octo_matrix):
        self.matrix = octo_matrix
        self.range_ = (range(len(octo_matrix[0])), range(len(octo_matrix)))

    @classmethod
    def from_input(cls, path: str):
        """Create grid from input."""
        grid = [[Octopus(int(n)) for n in line.strip()] for line in open(path, 'r')]
        print(f"{grid=}")
        return cls(grid)

    def boost_all(self):
        """Boost all octo's in grid."""
        for y, octo_row in enumerate(self.grid):
            for x, octo in enumerate(octo_row):
                octo.get_boost()
                if octo.energy_level > 9:
                    octo.energy_level = 0
                    neighbours = octo.get_neighbours()
                    self.boost(neighbours)

    @staticmethod
    def boost(neighbours):
        """Boost neighbours."""
        for (x, y) in neighbours:
            self.grid[y][x].get_boost()
            new_neighbours = _
            if octo.energy_level > 9:
                octo.energy_level = 0
                new_neighbours = octo.get_neighbours()
                self.boost(new_neighbours)




def stepper():
    """Go through steps."""
    # Loop throug grid and


def main():
    input_file = sys.argv[1] if len(sys.argv) > 1 else '11.in'
    grid = OctopusGrid.from_input(input_file)


if __name__ == "__main__":
    main()

