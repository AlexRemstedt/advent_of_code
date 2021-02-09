# Input
file = open('input_files/day_1_input', 'r')  # Opens file
entries_list = list(map(int, file.readlines()))  # Saves file into list
file.close()


# Function
def find_2020_i(entries):
    for entry1 in entries:
        for entry2 in entries:
            if entry1 + entry2 == 2020:
                return entry1 * entry2


print(f'Answer part i: {find_2020_i(entries_list)}')  # Part 1


def find_2020_ii(entries):
    for entry1 in entries:
        for entry2 in entries:
            for entry3 in entries:
                if entry1 + entry2 + entry3 == 2020:
                    return entry1 * entry2 * entry3


print(f'Answer part ii: {find_2020_ii(entries_list)}')
