"""Day 6: Lanternfish."""

def from_input(path_to_file='./inputs/6_Lanternfish'):
    """Get data from input."""
    with open(path_to_file, 'r') as f:
        [raw] = [l.split() for l in f]
    [raw] = [string.split(',') for string in raw]
    raw = [int(num) for num in raw]
    return raw

def main():
    initial_state = from_input()
    
    lantern_fish = initial_state.copy()
    days = [*range(1, 81)]
    for day in days:
        for n, fish in enumerate(lantern_fish):
            lantern_fish[n] -= 1
            if fish == 0:
                lantern_fish.append(9)
                lantern_fish[n] = 6
    print(len(lantern_fish))

if __name__ == "__main__":
    main()


