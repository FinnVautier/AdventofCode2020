'''

Day 15: Rambunctious Recitation

'''
from collections import Counter



## Part 1 ##
test_input = [0, 3, 6]

def rambunctious(test_input):
    turn = 0
    starting_num_len = len(test_input)
    while turn < 2020:
        if turn < starting_num_len:

            turn += 1
        else:


            cou = Counter(test_input)

            last_num = test_input[turn - 1]
            ## If number is has been spoken before

            if cou[test_input[turn-1]] > 1:
                res_list = [i for i in range(len(test_input)) if test_input[i] == last_num]
                dif_last_spoken = res_list[-1] - res_list[-2]
                test_input.append(dif_last_spoken)


            ## If number is new
            elif cou[test_input[turn-1]] == 1:
                test_input.append(0)

            ##Increment turn
            turn += 1

    return test_input[-1]

## Evaluating model on all of the test inputs to find accuracy
test_input1 = [1, 3, 2]
print('The 2020th output for : [1,3,2] is : {} '.format(rambunctious(test_input1)))

test_input2 = [2, 1, 3]
print('The 2020th output for : [2,1,3] is : {} '.format(rambunctious(test_input2)))

test_input3 = [1, 2, 3]
print('The 2020th output for : [1,2,3] is : {} '.format(rambunctious(test_input3)))

test_input4 = [2, 3, 1]
print('The 2020th output for : [2,3,1] is : {} '.format(rambunctious(test_input4)))

test_input5 = [3, 2, 1]
print('The 2020th output for : [3,2,1] is : {} '.format(rambunctious(test_input5)))

test_input6 = [3, 1, 2]
print('The 2020th output for : [3,1,2] is : {} '.format(rambunctious(test_input6)))

pt1_input = [0, 6, 1, 7, 2, 19, 20]
print('The 2020th output for : [0,6,1,7,2,19,20] is : {}'.format(rambunctious(pt1_input)))

## Part 2 ## - 1st Attempt
def rambunctious_pt2(test_input):
    turn = 0
    starting_num_len = len(test_input)
    while turn < 30000000:
        if turn < starting_num_len:
            turn += 1
        else:

            cou = Counter(test_input)

            last_num = test_input[turn - 1]

            ## If number is has been spoken before
            if cou[test_input[turn-1]] > 1:
                # This loooping through all the list causes a large timecomplexity
                res_list = [i for i in range(len(test_input)) if test_input[i] == last_num]
                dif_last_spoken = res_list[-1] - res_list[-2]
                test_input.append(dif_last_spoken)


            ## If number is new
            elif cou[test_input[turn-1]] == 1:
                test_input.append(0)

            ##Increment turn
            turn += 1

    return test_input[-1]

#print('Part 2 2020th Output for [0,3,6] is: {}'.format(rambunctious_pt2(test_input)))

## Part 2 ## 2nd Attempt fix

def rambunctious_pt2_1(test_input, input_size):
    # Looping through the length of test_input each time to find the most recent index is not efficient at all
    # However, keeping a dictionary is only o(1) complexity, where as looping through a list is o(n) complexity
    # We could use a dictionary to store the index of the most recent position of a number in the list

    memory = {}

    for i in range(len(test_input)-1):
        num = test_input[i]
        memory[num] = i

    for i in range(len(test_input) -1, input_size -1):
        num = test_input[i]

        if num not in memory:
            test_input.append(0)
            memory[num] = i

        else:
            ## Find the previous index of the number in memory
            prev_index = memory[num]
            ## Append the difference between current index and previous index
            new_num = i - prev_index
            test_input.append(new_num)
            ## Update the memory with most recent position of the index
            memory[num] = i

    return test_input[-1]

pt2_input = [0, 6, 1, 7, 2, 19, 20]
print(rambunctious_pt2_1(pt2_input, 30000000))
