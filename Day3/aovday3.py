'''

Advent of Code 3

'''

toboggan =  open("aovday3input.txt").read().splitlines()

map_basis = toboggan

total_trees = []

def is_there_a_tree(hill_x, hill_y):
    map_x = hill_x % 31
    return map_basis[hill_y][map_x] == '#'

def tree_count_for_slope(right_move, down_move):
    x_coordinate = 0
    y_coordinate = 0
    tree_count = 0

    while y_coordinate < len(map_basis):
        if is_there_a_tree(x_coordinate, y_coordinate):
            tree_count += 1
        y_coordinate += down_move
        x_coordinate += right_move

    print(tree_count)
    total_trees.append(tree_count)

tree_count_for_slope(1,1)
tree_count_for_slope(3,1)
tree_count_for_slope(5,1)
tree_count_for_slope(7,1)
tree_count_for_slope(1,2)

## Part 2
total = 1
for item in total_trees:
    total *= item

print(total)
