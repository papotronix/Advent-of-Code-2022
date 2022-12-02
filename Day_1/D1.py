import time
start = time.time()

calories = open('Day_1/input.txt', 'r', newline=None).read().split('\n')
#print(calories)

## Part 1
calorie_list = [[]]
elf_counter = 0
for n in calories:
    if n != '':
        calorie_list[elf_counter].append(n)
    else:
        elf_counter += 1
        calorie_list.append([])

#print(calorie_list)

# The most calories carried by any one elf
calorie_total_per_elf = [sum([int(food_calories) for food_calories in food_calorie_sublist]) for food_calorie_sublist in calorie_list]
print(max(calorie_total_per_elf))

# The elf carrying the most calories is
print(calorie_total_per_elf.index(max(calorie_total_per_elf)) + 1) 

## Part 2
# Sum of calories carried by the top three elves
top_three_elves = sorted(calorie_total_per_elf)[-3:]
print(sum(top_three_elves))

end = time.time()
print("Execution time: ", end - start)