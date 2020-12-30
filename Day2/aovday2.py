'''

Advent of Code Day 2

'''

expense_list =  open("aovday2input.txt").read().splitlines()

expense_list = [list(i.split(" ")) for i in expense_list]

good_password = []

for item in expense_list:
    position_1 = int(item[0].split("-")[0])
    position_2 = int(item[0].split("-")[1])
    letter = item[1].replace(":", "")

    if bool(item[2][position_1 -1] == letter) != bool(item[2][position_2 - 1] == letter):
        good_password.append(item)


print('Answer to Part 2:', len(good_password))
