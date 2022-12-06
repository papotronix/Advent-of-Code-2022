import time
import re
import copy

start = time.time()

## Part 1

# Parse input
input = open('Day_5/input.txt', 'r', newline=None).read().split('\n\n')
raw_stacks = input[0].split('\n')
movement_steps = input[1].split('\n')

for i in range(len(raw_stacks)):
    raw_stacks[i] = raw_stacks[i].replace('    ', ' ')
#print(input_boxes)

box_columns = []
for i in range(len(raw_stacks)-1):
    box_columns.append(raw_stacks[i].split(' '))
#print(boxes_vertical)


box_rows_1 = [[] for i in range(len(box_columns[0]))]
for i in range(len(box_columns)):
    for j in range(len(box_columns[i])):
        if(box_columns[i][j] != ''):
            box_rows_1[j].append(box_columns[i][j]) 
#print(box_rows_1)
box_rows_2 = copy.deepcopy(box_rows_1)

# Remove non-numeric characters from movement_steps
for i in range(len(movement_steps)):
    movement_steps[i] = re.sub('[^0-9 ]', '', movement_steps[i])
    movement_steps[i] = movement_steps[i].split()
#print(movement_steps)

# Convert movement_steps to integers
for i in range(len(movement_steps)):
    movement_steps[i] = [int(j) for j in movement_steps[i]]
# print(movement_steps)

# Execute steps of moving the boxes
# Index 0 is the number of boxes to move
# Index 1 is the stack to move the boxes from
# Index 2 is the stack to move the boxes to
for command in range(len(movement_steps)): # for each step/command
    for i in range(movement_steps[command][0]): # For each box to move according to the command
        box_rows_1[movement_steps[command][2]-1].insert(0,box_rows_1[movement_steps[command][1]-1][0])
        box_rows_1[movement_steps[command][1]-1].pop(0)
    
#print(box_rows_1)

for stack in box_rows_1:
    print(re.sub(r'[^\w]', '', stack[0]),end='')
print('\n',)

## Part 2

# Execute steps of moving the boxes
# Index 0 is the number of boxes to move
# Index 1 is the stack to move the boxes from
# Index 2 is the stack to move the boxes to
for command in range(len(movement_steps)): # for each step/command
    if(movement_steps[command][0] == 1): # If only moving one box, same as part 1
        # print(boxes_horizontal[movement_steps[command][1]-1][0])
        box_rows_2[movement_steps[command][2]-1].insert(0,box_rows_2[movement_steps[command][1]-1][0])
        box_rows_2[movement_steps[command][1]-1].pop(0)
    else: # If moving more than one box
        subset = box_rows_2[movement_steps[command][1]-1][0:(movement_steps[command][0])]
        for box in reversed(subset):
            box_rows_2[movement_steps[command][2]-1].insert(0,box)
            box_rows_2[movement_steps[command][1]-1].pop(0)

#print(box_rows_2)
for stack in box_rows_2:
    print(re.sub(r'[^\w]', '', stack[0]),end='')
print('\n',)

end = time.time()
print("Execution time: ", end - start)