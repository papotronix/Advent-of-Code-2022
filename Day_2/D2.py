import time
start = time.time()

strategy_list = open('Day_2/input.txt', 'r', newline=None).read().replace(" " ,"").split('\n')
#print(strategy)

## Part 1
score_map_1 = {
    'AX': 4, 'AY': 8, 'AZ': 3, 
    'BX': 1, 'BY': 5, 'BZ': 9,
    'CX': 7, 'CY': 2, 'CZ': 6
}

total_score = 0
for round in strategy_list:
    total_score += score_map_1[round]

print(total_score)

## Part 2

score_map_2 = {
    'AX': 3, 'AY': 4, 'AZ': 8, 
    'BX': 1, 'BY': 5, 'BZ': 9,
    'CX': 2, 'CY': 6, 'CZ': 7
}

total_score = 0
for round in strategy_list:
    total_score += score_map_2[round]

print(total_score)


end = time.time()
print("Execution time: ", end - start)