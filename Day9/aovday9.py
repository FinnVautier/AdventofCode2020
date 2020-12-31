'''

Day 9 -- Advent of Code

'''

lines = open('aovday9input.txt').read().splitlines()

for i in range(0, len(lines)):
    lines[i] = int(lines[i])

preamble_length = 25

preamble = []

for i in range(0, preamble_length):
    preamble.append(lines[i])


def check_if_sum(preamble, num):
    sort = sorted(preamble)
    n = len(sort)
    left_pointer = 0
    right_pointer = n - 1
    while left_pointer < right_pointer:
        if sort[left_pointer] + sort[right_pointer] == num:
            return True
        elif sort[left_pointer] + sort[right_pointer] < num:
            left_pointer += 1
        elif sort[left_pointer] + sort[right_pointer] > num:
            right_pointer -= 1

    return False

def iterate_through_input():
    for j in range(preamble_length, len(lines)):

        if check_if_sum(preamble, lines[j]):
            preamble.append(lines[j])
            preamble.pop(0)

        else:
            pt1_ans = "The first number that doesn't have this property is: {}".format(lines[j])
            return pt1_ans



## Part 2 - Find Contiguous Subarray that produces a sum equal to that in part 1.

def subArraySum(lines, desired_total):

    n = len(lines)
    curr_sum = 0

    for i in range(len(lines)):

        curr_sum = lines[i]

        j = i + 1

        while j <= n:

            if curr_sum == desired_total:
                print('Sum of the Maximum and Minimum values in the subarray:' ,max(lines[i:j-1]) + min(lines[i:j-1]))
                return True
            elif curr_sum > desired_total or j == n:
                break

            curr_sum = curr_sum + lines[j]

            j += 1

    return False

print('-- Part 1 - Answer --')
print(iterate_through_input())
print('-- Part 2 - Answer --')
subArraySum(lines, 22477624)