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
from typing import Tuple

class Octopus:
    """Hold energylevels."""

    def __init__(self, initial_energy_level):
        self.energy_level = initial_energy_level
        self.flashed = False

    def get_boost(self):
        "Give boost to Octopus."""
        self.energy_level += 1
        return "BOOOST"

    def flash(self):
        """Octopus is flash."""
        if self.energy_level > 9 and not self.flashed:
            self.flashed = True
            return True

    @staticmethod
    def get_neighbours(center: Tuple, range_):
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
            new_x = center[0] + x
            new_y = center[1] + y
            # TODO: Check range here?
            if new_x in range_[0] and new_y in range_[1]:
                neighbours.append((new_x, new_y))
        return neighbours


class OctopusGrid:
    """Hold octopus positions."""

    def __init__(self, octo_matrix):
        """Initialise grid."""
        self.matrix = octo_matrix
        self.range_ = (range(len(octo_matrix[0])), range(len(octo_matrix)))
        self.flashes: int = 0

    @classmethod
    def from_input(cls, path: str):
        """Create grid from input."""
        grid = [[Octopus(int(n)) for n in line.strip()] for line in open(path, 'r')]
        return cls(grid)

    def boost_all(self):
        """Boost all octo's in grid."""
        for y, octo_row in enumerate(self.matrix):
            for x, octo in enumerate(octo_row):
                octo.get_boost()
                if octo.flash:
                    self.flashes += 1
        return "Grid boosted"

    def boost_surrounding(self, neighbours):
        """Boost neighbours."""
        for (x, y) in neighbours:
            self.matrix[y][x].get_boost()
            # new_neighbours = _
            if self.matrix[y][x].flash():
                self.flashes += 1
                new_neighbours = self.matrix[y][x].get_neighbours((x, y), self.range_)
                self.boost_surrounding(new_neighbours)
        return "Grid boosted"

    def reset_flash(self):
        for y, octo_row in enumerate(self.matrix):
            for x, octo in enumerate(octo_row):
                if octo.energy_level > 9:
                    octo.energy_level = 0 
    
    def show(self):
        """Show the grid in the same way it is on AoC."""
        octo_grid = []
        for octo_line in self.matrix:
            octo_print = []
            for octopus in octo_line:
                octo_print.append(octopus.energy_level)
            print(octo_print)


def stepper(grid):
    """Go through steps."""
    # TODO: Loop throug grid and
    steps = 10
    for step in range(1, steps):
        print(f"After {step=}")

        # Correct order:
        # 1. Energy level of each Octo increase
        # 2. Any octo with energy_level > 9 flash
        # 3. Increase level surrounding flash
        # 4. Repeat step 2-3 until all flashes have been flashed.
        grid.boost_all()
        # 5. Set flashed to 0
        grid.reset_flash()

        # Boost full grid -> This also handles neighbours who flash.

        grid.show()

    return "Fully stepped"


def main():
    input_file = sys.argv[1] if len(sys.argv) > 1 else '11.in'
    grid = OctopusGrid.from_input(input_file)
    stepper(grid)


if __name__ == "__main__":
    main()

