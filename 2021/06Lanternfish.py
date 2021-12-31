"""Day 6: Lanternfish."""

from collections import defaultdict

def from_input(path_to_file='./inputs/6_Lanternfish'):
    """Get data from input."""
    with open(path_to_file, 'r') as f:
        raw = [int(num) for num in f.read().strip().split(',')]
    return raw

def part1():
    initial_state = from_input()
    
    DAYS = 80
    lantern_fish = initial_state.copy()
    for day in range(DAYS):
        for n, fish in enumerate(lantern_fish):
            lantern_fish[n] -= 1
            if fish == 0:
                lantern_fish.append(9)
                lantern_fish[n] = 6
    return len(lantern_fish)


def part2():
    initial_state = from_input()

    lantern_fish = initial_state.copy()

    fish_map = {}
    for fish in lantern_fish:
        if fish not in fish_map:
            fish_map[fish] = 0
        fish_map[fish] += 1

    DAYS = 256

    for day in range(DAYS):
        up_fish_map = defaultdict(int)  # Avoids KeyError

        # Go to each fish to change its state.
        for fish, count in fish_map.items():
            if fish == 0:
                up_fish_map[6] += count
                up_fish_map[8] += count
            else:
                up_fish_map[fish - 1] += count
        
        fish_map = up_fish_map
    return(sum(fish_map.values()))

if __name__ == "__main__":
    print(part1())
    print(part2())


