"""Day 11: Dumbo Octopus."""

import sys
import numpy as np
from listing import Tuple

class Octopus:
    """Octopus object."""

    def __init__(self, energy_level: int, coordinates: Tuple[int]):
        self.energy_level = energy_level
        self.coordinates = coordinates

    def increase_value(self):
        """Increase energy level by one."""
        self.energy_level += 1

    def get_surrounding(self, grid):
        """Get all the surrounding octopi positions."""
        coords = []
        boundaries = (0, 9)
        rows = list(range(j - 1, j + 2))
        cols = list(range(i - 1, i + 2))
        for y in rows:
            if y in list(range(boundaries)):
                for x in cols:
                    if x in list(range(boundaries)):
                        coords.append((x, y))
        coords.remove((i, j))
        return coords


class EnergyGrid:

    def __init__(self, grid):
        self.grid = grid

    @classmethod
    def from_input(cls, input_file):
        """Create grid from input."""
        grid = []
        for j, line in enumerate(open(input_file)):
            n_line = []
            for i, value in enumerate(line.strip()):
                octo = Octopus(int(value), (i, j))
                n_line.append(octo)
            grid.append(n_line)
        return cls(grid)

    def increase_energy(self):
        """Increase all energylevels by 1."""
        for line in self.grid:
            for point in line:
                point.increase_value()

    def flash(i, j):
        """Add one energy-level to surrounding values."""
        # center numbers
        # edge numbers

    def check_flash(self):
        """Check for flashes."""
        joint 
        for j, line in enumerate(self.grid):
            for i, value in enumerate(line):
                if value.flashes():
                    surrounding = value.get_surrounding()
                    for coord in surrounding:
                        coord.increase_value()


def protocol(grid):
    """Cycle through protocols."""
    # step 1: Energy level of each octopus increase by 1.
    grid.increase_energy()
    # step 2: If energylevel > 9: Flash
    grid.check_flash()
    return None


def part1(input_file):
    full_grid = EnergyGrid.from_input(input_file)
    protocol(full_grid)


def main():
    input_file = sys.argv[1] if len(sys.argv) > 1 else '10.in'
    part1(input_file)

if __name__ == '__main__':
    main()
