"""Day 11: Dumbo Octopus."""

import sys
import numpy as np

class EnergyGrid:

    def __init__(self, input_file):
        self.input_file = input_file
        self.grid = self.make_grid()
    
    def make_grid(self):
        """Make a grid of octopi-energy-levels."""
        octopi = []
        for line in open(self.input_file):
            energy_levels = [int(octopus) for octopus in line.strip()]
            octopi.append(energy_levels)
        return octopi

    def increase_energy(self):
        """Increase the energylevels by 1."""
        self.grid = np.array(self.grid) + 1
        self.check_flash()

    def check_flash(self):
        if 9 in self.grid:
            get_index()
        for line in self.grid:
            print(number)


def part1(input_file):
    octopussy = EnergyGrid(input_file)
    octopussy.increase_energy() 


def main():
    input_file = sys.argv[1] if len(sys.argv) > 1 else '10.in'
    part1(input_file)

if __name__ == '__main__':
    main()
