"""Day 3: Binary Diagnostic.

What is the power consumption of the submarine.
Verify the life support rating.
"""

# --- Part One ---
# with open("inputs/3_BinaryDiagnostic", 'r') as raw_data:
    # bits = [line for line in raw_data]
    # biggest_bit = ""
    # smallest_bit = ""
    # for n in range(len(bits[0]) - 1):
        # biggest_bit += str(int(len(bits) / 2 < sum(int(bit[n]) for bit
            # in bits)))
        # smallest_bit += str(int(len(bits) / 2 > sum(int(bit[n]) for bit
            # in bits)))
    
    # gamma_rate = int(biggest_bit, 2)
    # epsilon_rate = int(smallest_bit, 2)
    # print(f"Part One: {epsilon_rate * gamma_rate}")

# --- Part Two ---
with open("./inputs/3_BinaryDiagnostic", 'r') as raw_data:
    bits = [line.strip('\n') for line in raw_data]
    biggest_bit = ""
    smallest_bit = ""
    for n in range(len(bits[0])):
        smallest_bit += str(int(len(bits) / 2 >= sum(int(bit[n]) for bit
            in bits)))

    oxygen_gen_rating = [bit for bit in bits]
    CO2_scrubber_rating = [bit for bit in bits]

    def biggest_bit(lst, idx):
        bit_master = str(int(len(lst) / 2 <= sum(int(bit[idx]) for bit in lst)))
        return bit_master

    def smallest_bit(lst, idx):
        bit_master = str(int(len(lst) / 2 > sum(int(bit[idx]) for bit in lst)))
        return bit_master

    for idx in range(len(oxygen_gen_rating[0])):
        to_be_removed = []
        checker = biggest_bit(oxygen_gen_rating, idx)
        for n, bit in enumerate(oxygen_gen_rating):
            if checker != bit[idx]:
                to_be_removed.append(n)
        if len(oxygen_gen_rating) > 1:
            for remove in to_be_removed[::-1]:
                oxygen_gen_rating.pop(remove)

    for idx in range(len(CO2_scrubber_rating[0])):
        to_be_removed = []
        checker = smallest_bit(CO2_scrubber_rating, idx)
        for n, bit in enumerate(CO2_scrubber_rating):
            if checker != bit[idx]:
                to_be_removed.append(n)
        if len(CO2_scrubber_rating) > 1:
            for remove in to_be_removed[::-1]:
                CO2_scrubber_rating.pop(remove)

    print(int(oxygen_gen_rating[0], 2) * int(CO2_scrubber_rating[0], 2))


