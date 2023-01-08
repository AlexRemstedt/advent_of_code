"""Day 2: Rock Paper Scissors"""
import sys

# X = lose
# Y = draw
# Z = win

#          Rock Paper Scissors
# Z you win: B    C     A
# Y you draw: A    B     C
# X you lose: C    A     B


def main(path):
    i = [x.strip() for x in open(path)]
    total_score = 0
    for x in i:
        opponent, outcome = x.split()
        score = {'X': 0, 'Y': 3, 'Z': 6}[outcome]  # win/draw/lose
        score += {('A', 'X'): 3, ('A', 'Y'): 1, ('A', 'Z'): 2,
                  ('B', 'X'): 1, ('B', 'Y'): 2, ('B', 'Z'): 3,
                  ('C', 'X'): 2, ('C', 'Y'): 3, ('C', 'Z'): 1}[(opponent, outcome)]
        total_score += score
    print(total_score)


if __name__ == "__main__":
    input_file = sys.argv[1] if len(sys.argv) > 1 else '02.x'
    main(input_file)
