"""Day 1: Calorie Counting."""
import sys


class Elf:
    """Elf object which contains an amount of calories."""

    def __init__(self, packages):
        self.packages = packages
        self.calories = sum(packages)


def main(data_file):
    """Data:
    1000
    2000
    3000

    4000

    5000
    6000

    7000
    8000
    9000

    10000
    """
    # ["1000", "2000", "3000", "", "4000", "", "5000", "6000", "", "7000", "8000", "9000", "", "10000"]
    data = [x.strip() for x in open(data_file)]

    # [Elf objects]
    elves = []
    caloriestack = []
    for val in data:
        if val != "":
            caloriestack.append(float(val))
        else:
            elf = Elf(caloriestack)
            elves.append(elf)
            caloriestack = []

    elf = Elf(caloriestack)
    elves.append(elf)

    print(f"part 1: {max([elf.calories for elf in elves])}")
    print(f"part 2: {sum(sorted([elf.calories for elf in elves], reverse=True)[:3])}")


if __name__ == "__main__":
    input_file = sys.argv[1] if len(sys.argv) > 1 else '01.x'
    main(input_file)

###############################################################################

# # Dit is de calculator
# def calculate_calories(calories):
#     return None
#     # return sum_of_calories


# def max_calorie_finder(elves):
#     """Find the caloriestack with the biggest amount of cal's in his caloriestack."""
#     max_calories = 0
#     for caloriestack in elves:
#         block_calories = calculate_calories(caloriestack)
#         if block_calories >= max_calories:
#             max_calories = block_calories


