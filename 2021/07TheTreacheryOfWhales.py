"""Day 7: The Treachery of Whales."""


def get_input(path_to_file='./inputs/7_TheTreacheryOfWhales'):
    with open(path_to_file, 'r') as f:
        raw = [int(num) for num in f.read().strip().split(',')]
    return raw

def part1():
    positions = get_input()
    max_pos = max(positions)
    min_pos = min(positions)

    old_fuel = max_pos * len(positions)
    for average_position in range(min_pos, max_pos):
        fuel = 0
        for position in positions:
            fuel += abs(average_position - position)
        if old_fuel > fuel:
            old_fuel = fuel
    return old_fuel


def part2():
    positions = get_input()
    max_pos = max(positions)
    min_pos = min(positions)

    old_fuel = 1000000000000000
    for average_position in range(min_pos, max_pos):
        fuel = 0
        for position in positions:
            x = abs(average_position - position)
            fuel += x * (x + 1) / 2
        if old_fuel > fuel:
            old_fuel = fuel
    return old_fuel

if __name__ == "__main__":
    print(part1())
    print(part2())


