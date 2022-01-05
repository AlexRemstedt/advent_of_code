#!/venv/bin/python
"""Day 8: Seven Segment Search."""

import itertools
from collections import defaultdict 

def get_input(path_to_file='./inputs/8_SevenSegmentSearch'):
    with open(path_to_file, 'r') as f:
        raw = f.readlines()
    raw = [line.split('|')[1].strip() for line in raw]
    raw = [words.split() for words in raw]
    return raw


def part1():
    lines = get_input()

    ez_digits = [2, 4, 3, 7]
    count = 0
    for digits in lines: 
        for digit in digits:
            if len(digit) in ez_digits:
                count += 1
    return count



# def part1(path_to_file='./inputs/8_SevenSegmentSearch'):
    # ans = 0
    # for line in open(path_to_file, 'r'):
        # before, after = line.split('|')
        # before = before.split()
        # after = after.split()
        # # Store lengths and words.
        # by_len = defaultdict(list)
        # for word in before:
            # by_len[len(word)].append(word)
        # for word in after:
            # # If word is unique, then there is only 1 of them.
            # if len(by_len[len(word)]) == 1: 
                # ans += 1
    # print(ans)


def part2(path_to_file='./inputs/8_SevenSegmentSearch'):
    """Part 2 inspired by https://youtu.be/DhQPrF-LBoE."""

    digits = {
        0: 'abcefg',
        1: 'cf',
        2: 'acdeg',
        3: 'acdfg',
        4: 'bcdf',
        5: 'abdfg',
        6: 'abdefg',
        7: 'acf',
        8: 'abcdefg',
        9: 'abcdfg'
    }

    def find_perm_slow(before):
        """Permutations cycles through all possible translations."""
        for perm in itertools.permutations(list(range(8))):
            translate_dictionary = {}
            correct_dictionary = True
            for i in range(8):
                # Create a 'translate dictionary'
                translate_dictionary[chr(ord('a') + i)] = chr(ord('a') + perm[i])

            # Create a translation of the words using current dictionary.
            for word in before:
                translation = ''
                for character in word: 
                    translation += translate_dictionary[character]
                translation = ''.join(sorted(translation))  # sort characters.
                # Check if translation is readable.
                if translation not in digits.values():
                    correct_dictionary = False

            if correct_dictionary:
                return translate_dictionary

    def find_perm(before):
        translate_dictionary = {}

        for word in before:
            # Find translations of c and f.
            if len(word) == 2:
                cf = word
        assert len(cf) == 2, cf
        
        # Put f and c in the correct position.
        for word in before:
            if len(word) == 6 and (cf[0] in word) != (cf[1] in word):
                if cf[0] in word:
                    translate_dictionary[cf[0]] = 'f'
                    translate_dictionary[cf[1]] = 'c'
                else:
                    translate_dictionary[cf[1]] = 'f'
                    translate_dictionary[cf[0]] = 'c'
        assert len(translate_dictionary) == 2, f'{translate_dictionary=} {cf=} {before}'
        
        for word in before:
            # Find translation of the a-position.
            if len(word) == 3:
               for char in word:
                   if char not in cf:
                        translate_dictionary[char] = 'a'
        assert len(translate_dictionary) == 3, translate_dictionary

        for word in before:
            if len(word) == 4:
                # Translation of b and d.
                bd = ''
                for char in word:
                    if char not in cf:
                        bd += char
        assert len(bd) == 2, bd

        # Put b and d in right position.
        for word in before:
            if len(word) == 6 and (bd[0] in word) != (bd[1] in word):
                if bd[0] in word:
                    translate_dictionary[bd[0]] = 'b'
                    translate_dictionary[bd[1]] = 'd'
                else:
                    translate_dictionary[bd[1]] = 'b'
                    translate_dictionary[bd[0]] = 'd'
        assert len(translate_dictionary) == 5, translate_dictionary

        eg = ''
        for char in ['a', 'b', 'c', 'd', 'e', 'f', 'g']:
            if char not in translate_dictionary:
                eg += char
        assert len(eg) == 2, eg 

        for word in before:
            if len(word) == 6 and (eg[0] in word) != (eg[1] in word):
                if eg[0] in word:
                    translate_dictionary[eg[0]] = 'g'
                    translate_dictionary[eg[1]] = 'e'
                else:
                    translate_dictionary[eg[1]] = 'g'
                    translate_dictionary[eg[0]] = 'e'
        assert len(translate_dictionary) == 7, translate_dictionary
        return translate_dictionary


    ans = 0
    for line in open(path_to_file, 'r'):
        before, after = line.split('|')
        before = before.split()
        after = after.split()
    
        translate_dictionary = find_perm(before)
        after_digit = ''
        # Translate after-words.
        for word in after:
            translation = ''
            for character in word: 
                translation += translate_dictionary[character]
            translation = ''.join(sorted(translation))  # sort characters.
            # Find correct digit for translation.
            digit = []
            for key, value in digits.items():
                if value == translation:
                    digit.append(key)
            # digit = [key for key, value in digits.items() if value == translation]
            assert len(digit) == 1
            after_digit += str(digit[0])
        ans += int(after_digit)
    print(ans)


if __name__ == "__main__":
    part1()
    part2()

