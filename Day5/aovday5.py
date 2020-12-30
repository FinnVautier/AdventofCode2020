'''

Advent of Code Day 5

By : Finn Vautier 
'''


## 128 Rows on the Plane - each character F or B - Front or Back
## e.g. First Letter - 0-63 Front or 64-127 Back 

boarding_passes =  open("aovday5input.txt").read().splitlines()

seat_id_list = []

for item in boarding_passes:
    row_count = [0,0,0,0,0,0,0]
    column_count = [0,0,0]
    
    ## Row Check 
    ## Check the rows 
    for i in range(0, 7):

        if item[i] == 'F':
            row_count[i] = '0'

        elif item[i] == 'B':
            row_count[i] = '1'
           
    row_result = int("".join(str(x) for x in row_count), 2)

    ## Column Check 
    ## Check Columns
    
    for j in range(7,10):
        
        if item[j] == 'R':
            column_count[j - 7] = '1'

        elif item[j] == 'L':
            column_count[j - 7] = '0'

    ## Convert Check Column Binary to Decimal 
    column_result = int("".join(str(x) for x in column_count), 2)
    

    seat_id = row_result * 8 + column_result
    seat_id_list.append(seat_id)

print('Maximum Seat Id:', max(seat_id_list))

## Part 2 - Find the missing number in the sequence of seat IDs. 
def find_missing(lst): 
    return sorted(set(range(lst[0], lst[-1])) - set(lst)) 

print(find_missing(seat_id_list))

