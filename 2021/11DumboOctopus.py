"""Day 11: Dumbo Octopus."""

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
        return "Grid boosted"

    def flasher_check(self):
        """Check grid for flashers."""
        for y, octo_row in enumerate(self.matrix):
            for x, octo in enumerate(octo_row):
                # check if octo.energy_level > 9 and not yet flashed
                if self.matrix[y][x].flash():
                    # Boost all surrounding
                    neighbours = octo.get_neighbours((x, y), self.range_)
                    self.boost_surrounding(neighbours)
        return "checked grid"

    def boost_surrounding(self, neighbours):
        """Boost neighbours."""
        for (x, y) in neighbours:
            neighbour = self.matrix[y][x]
            neighbour.get_boost()
            if neighbour.flash():
                new_neighbours = neighbour.get_neighbours((x, y), self.range_)
                self.boost_surrounding(new_neighbours)
        return "Neighbours boosted"

    def reset_flash(self):
        """Reset all flashed octi to 0."""
        for y, octo_row in enumerate(self.matrix):
            for x, octo in enumerate(octo_row):
                if octo.flashed:
                    self.flashes += 1
                    self.matrix[y][x].energy_level = 0 
                    self.matrix[y][x].flashed = False 
        return "Rest finally"
    
    def show(self):
        """Show the grid in the same way it is on AoC."""
        octo_grid = []
        for octo_line in self.matrix:
            octo_print = []
            for octopus in octo_line:
                octo_print.append(octopus.energy_level)
            print(octo_print)
        return "Showing grid"

    def sim_flash(self):
        """Check for simultaneous flash."""
        sum_ = 0
        for y in self.matrix:
            for x in y:
                sum_ += x.energy_level
        return not bool(sum_)


def stepper(grid):
    """Go through steps."""
    # TODO: Loop throug grid and
    steps = 1000
    for step in range(0, steps):
        # 1. Energy level of each Octo increase
        grid.boost_all()
        # 2. Any octo with energy_level > 9 flash
        # 3. Increase level surrounding flash
        grid.flasher_check()
        # 5. Set flashed to 0
        grid.reset_flash()
        if grid.sim_flash():
            print(f"{1+step=}")
    grid.show()
    print(grid.flashes)
    return "Fully stepped"


def main():
    # Part 1
    input_file = sys.argv[1] if len(sys.argv) > 1 else '11.in'
    grid = OctopusGrid.from_input(input_file)
    stepper(grid)

    # Part 2
    


if __name__ == "__main__":
    main()

