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


class OctopusGrid:
    """Hold octopus psitions."""

    def __init__(self, octo_matrix):
        self.matrix = octo_matrix

    @classmethod
    def from_input(cls, path):
        grid = [[Octopus(int(n)) for n in line.strip()] for line in open(path, 'r')]
        print(f"{grid=}")
        return cls(grid)

def main():
    input_file = sys.argv[1] if len(sys.argv) > 1 else '9.in'
    grid = OctopusGrid.from_input(input_file)

if __name__ == "__main__":
    main()

