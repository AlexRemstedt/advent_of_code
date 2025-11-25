brackets = []
while True:
    try:
        line = input()
        brackets.append(line)
    except EOFError:
        break

brackets = "".join(brackets)

plus = brackets.count("(")
minus = brackets.count(")")
print(plus - minus)


floor = 0
for n, x in enumerate(brackets, 1):
    if x == "(":
        floor += 1
    elif x == ")":
        floor -= 1
    if floor == -1:
        print(n)
        break
