"""Day 5: Hydrothermal Venture."""

from typing import List
import numpy as np


def data_manipulation(path_to_input='./inputs/5_HydrothermalVenture'):
    """Get data from inputfile."""
    # Main script
    with open(path_to_input, 'r') as f:
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

    
class Line:
    """Line object."""

    def __init__(self, point_1: List[float], point_2: List[float]):
        self.begin = tuple(point_1)
        self.end = tuple(point_2)

    def is_vertical(self):
        """Determine whether line is vertical."""
        return self.begin[0] == self.end[0]

    def is_horizontal(self):
        """Determine whether line is vertical."""
        return self.begin[1] == self.end[1]

    def is_diagonal(self):
        """Determine whether line is diagonal."""
        dx = self.begin[0] - self.end[0]
        dy = self.begin[1] - self.end[1]
        if dy/dx == 1 or dy/dx == -1:
            return dy/dx
        return False

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
                        max_ = value + 1
        return cls(size=(max_, max_))

    def draw_line(self, line: Line):
        """Draw line."""
        if line.is_horizontal(): 
            r = sorted([line.begin[0], line.end[0]])
            for point in range(r[0], r[1] + 1):
                self.grid[line.begin[1]][point] += 1

        elif line.is_vertical():  
            r = sorted([line.begin[1], line.end[1]])
            for point in range(r[0], r[1] + 1):
                self.grid[point][line.begin[0]] += 1

        elif line.is_diagonal() == 1:
            r = sorted([line.begin[0], line.end[0]])
            y_offset = line.begin[1] - line.begin[0]
            for point in range(r[0], r[1] + 1):
                self.grid[point + y_offset][point] += 1

        elif line.is_diagonal() == -1:
            r = sorted([line.begin[0], line.end[0]])
            y_offset = line.begin[1] - line.end[0]
            x = [*range(r[0], r[1] + 1)]
            y = x[::-1]
            y = [val + y_offset for val in y]
            for i, j in zip(x, y):
                self.grid[j][i] += 1

        else:  # Works
            return "No line drawn"
        return self.grid
        

def count_lines(grid: GridMap):
    big_numbers = 0
    for line in grid.grid:
        for number in line:
            big_numbers += int(number >= 2)
    return big_numbers


def main():
    """Main function."""
    basic_lines = data_manipulation('./inputs/5test')

    # Initialize grid
    grid = GridMap.from_lines(basic_lines)

    # Initialize lines
    lines = [Line(line[0], line[1]) for line in basic_lines]

    # Draw lines
    for line in lines:
        print(line.begin, line.end)
        print(grid.draw_line(line))
        input()
    print(count_lines(grid))


if __name__ == "__main__":
    main()

