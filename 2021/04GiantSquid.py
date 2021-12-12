"""Day 4: Giant Squid

What will your final score be if you choose the board that is guaranteed 
to win first?
"""

import numpy as np
import itertools 
from typing import List


def in_matrix(number, matrix):
    for i, row in enumerate(matrix):
        if number in row:
            return i, row.index(number)


def row_wins(matrix):
    ret = False
    for i, row in enumerate(matrix):
        ret += sum(row) == len(row)
        if ret:
            return ret, i
    return ret, i



def col_wins(matrix):
    ret = False
    for j, col in enumerate(matrix.transpose()):
        ret += sum(col) == len(col)
    return ret, j


class BingoCard:
    """Bingo card datatype."""

    def __init__(self, number_card, id_):
        self.marks = np.zeros(shape=(5, 5))
        self.values = number_card
        self.id = id_

    def print_mark(self):
        [print(row) for row in self.marks]
        print('')
        pass

    def print_card(self):
        [print(row) for row in self.marks]
        print('')
        pass


class BingoGame:
    
    def __init__(self, rolled_numbers: List[int]):  # should this be card or cards?
        self.rolled_numbers = rolled_numbers
        

    def marker(self, card: BingoCard):
        # Cycle through rolled numbers
        for rolled in self.rolled_numbers:
            markable = in_matrix(rolled, card.values)
            if markable:
                card.marks[markable[0]][markable[1]] = 1
                if row_wins(card.marks)[0] or col_wins(card.marks)[0]:
                    return self.rolled_numbers.index(rolled), card


def win_calcs(card: BingoCard):
    # find winning row
    s = 0
    for i, row in enumerate(card.marks):
        for j, _ in enumerate(row):
            if card.marks[i][j] == 0:
                s += card.values[i][j]
    return s



def import_():
    with open("inputs/4_GiantSquid", "r") as raw_data:
        input_ = [line for line in raw_data]
    return input_
        # Cards


def inp_cards(inp):
    """Create array of cards."""
    card_input = [row for row in inp[2:]]
    no_white_chars = [value.strip() for value in card_input]
    no_whitelines = list(filter(''.__ne__, no_white_chars))

    cards = [no_whitelines[i:i+5] for i in range(0, 
        len(no_whitelines), 5)]

    for card in cards:
        for n, row in enumerate(card):
            card[n] = row.split()
            for m, val in enumerate(card[n]):
                card[n][m] = int(val)

    return cards


def main():
    # Bingo cards
    cards = [BingoCard(card, id_) for id_, card in
            enumerate(inp_cards(import_()))]
    game = BingoGame([int(num) for num in import_()[0].split(',')])
    marked_cards = [game.marker(card) for card in cards]
    
    winning_card = marked_cards[0]
    for card in marked_cards:
        # for part 1 change < to >.
        if winning_card[0] < card[0]:
            winning_card = card
    x = win_calcs(winning_card[1])
    y = game.rolled_numbers[winning_card[0]]
    print(x * y)


if __name__ == "__main__":
    main()


    



# Notes
""" From stackoverflow:
```py
composite_list = [my_list[x:x+5] for x in range(0, len(my_list, 5)]
```
https://stackoverflow.com/q/15890743/14311374
"""
"""concept:
# def winner():
    # col_markerer
    # if col != marked and row != marked: 
        # return False

# for num in drawn_numbers:
    # for bingo_card in bingo_cards:
        # if winner(bingo_card):
            # print(num * 
# print(drawn_numbers)
"""
