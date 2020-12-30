'''

Advent of Code: Day 1
Author: Finn Vautier
'''


## PART 1

## Load Input
expense_list = list(map(int, open("aovday1.txt").read().splitlines()))

## First Solution - This is a slow brute force way of solving the problem - O(n^2)
def report_repair(lis):
    '''
    This function passes in the input for the expense report, and
    calculates which entries in the report sum to 2020. It then
    prints out the output.
    '''

    for i, item in enumerate(lis):
        for j in range(i+1, len(lis)):
            total_of_two = lis[i] + lis [j]
            if total_of_two == 2020:
                return lis[i] * lis[j]


report_repair(expense_list)

## Better Approach to Part 1 - Two Pointers Approach - Linear Time Complexity - O(n)

def report_repair_better(lis):
    '''
    This function is a better approach to solving task 1 as it
    has reduced time complexity. It uses a method called the two pointers
    approach, which works by first sorting the array and then moving
    two pointers; one at the last element, one at the first element.
    '''
    sort = sorted(lis)
    first_element = 0
    last_element = len(sort) - 1

    while first_element < last_element:
        if sort[first_element] + sort[last_element] == 2020:
            print(sort[first_element] * sort[last_element])
            return True
        elif sort[first_element] + sort[last_element] < 2020:
            first_element += 1
        else:
            last_element -= 1

report_repair_better(expense_list)

## PART 2

### Naive Approach - O(n^3) Time Complexity
def expense_triplet(lis):
    '''
    This function takes in the expense report as the input,
    it then calculates the triplet which sums together to
    equal 2020.
    '''
    length = len(lis)
    for i in range(0, length - 2):

        for j in range(i+1, length-1):

            for k in range(i+2, length):

                if lis[i] + lis[j] + lis[k] == 2020:
                    print(lis[i] * lis[j] * lis[k])
                    return True

expense_triplet(expense_list)

## Better Approach - This would have O(n) Linear Complexity
def expense_triplet_better(lis):
    '''

    This is a better approach to Part 2 as oppose to the
    brute force method shown above. This utilises the two pointer
    approach used in part 1

    '''

    sort = sorted(lis)
    for i in range(len(sort) - 2):
        first_element = i + 1
        last_element = len(sort) - 1

        while first_element < last_element:
            if sort[i] + sort[first_element] + sort[last_element] == 2020:
                print(sort[i] * sort[first_element] * sort[last_element])
                return True
            else:
                if sort[i] + sort[first_element] + sort[last_element] < 2020:
                    first_element += 1
                elif sort[i] + sort[first_element] + sort[last_element] > 2020:
                    last_element -= 1

expense_triplet_better(expense_list)
