file2 = open('input_files/day_2_input', 'r')  # Opens file
entries_list = list(map(str, file2.readlines()))  # Saves file into list
file2.close()


def password_checker_i(num):
    amount_passwords = 0
    for x in range(0, len(num)):
        loc1 = num[x].find('-')
        loc2 = num[x].find(' ')
        loc3 = num[x].find(':')

        lower_bound = int(num[x][0:loc1])
        upper_bound = int(num[x][loc1 + 1:loc2])
        letter = num[x][loc2 + 1:loc3]
        password = num[x][loc3 + 2:]

        letter_count = 0  # letter_count counts the occurences of letter in password
        for i in password:
            if i == letter:
                letter_count += 1

        if lower_bound <= letter_count <= upper_bound:
            amount_passwords += 1
    return amount_passwords


print(f'Part I - Amount of correct passwords: {password_checker_i(entries_list)}')


def password_checker_ii(num):
    amount_passwords = 0
    for x in range(0, len(num)):
        loc1 = num[x].find('-')
        loc2 = num[x].find(' ')
        loc3 = num[x].find(':')

        lower_bound = int(num[x][0:loc1]) - 1
        upper_bound = int(num[x][loc1 + 1:loc2]) - 1
        letter = num[x][loc2 + 1:loc3]
        password = num[x][loc3 + 2:]

        if password[lower_bound] == letter or password[upper_bound] == letter:
            if password[lower_bound] != password[upper_bound]:
                amount_passwords += 1

    return amount_passwords


print(f'Part II - Amount of correct passwords: {password_checker_ii(entries_list)}')
