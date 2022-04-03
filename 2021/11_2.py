"""Day 11: Dumbo Octopus."""

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
    def from_input(cls, input_):
        grid = _
        return cls(grid)

