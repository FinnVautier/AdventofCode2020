''' 

Advent of Code Day 6: Custom Customs

By: Finn Vautier

'''

from itertools import islice


##Part 1 

groups = open('aovday6input.txt').read().split('\n\n')

question_count = []

for group in groups:
    text = group.replace('\n', '')
    answers = set(text)
    question_count.append(len(answers))

print('Part 1 Count:', sum(question_count))


## Part 2 
from collections import Counter
question_counter = []

for group in groups:
    question_count = 0
    text = group.replace('\n', '')
    group_split = group.replace('\n', ' ').split(' ')
    length = len(group_split)
    count = Counter(text)
    for key, value in count.items():
        if count[key] == length:
            question_count += 1

    question_counter.append(question_count)

print('Part 2 Count:', sum(question_counter))