import time
start = time.time()


rucksack_input = open('Day_3/input.txt', 'r', newline=None).read().split('\n')
#print(rucksack_input)

## Part 1

# Define a map for the item priorities
priority_map = {
    'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8, 'i': 9, 'j': 10,
    'k': 11, 'l': 12, 'm': 13, 'n': 14, 'o': 15, 'p': 16, 'q': 17, 'r': 18, 's': 19, 
    't': 20,'u': 21, 'v': 22, 'w': 23, 'x': 24, 'y': 25, 'z': 26,
    'A': 27, 'B': 28, 'C': 29, 'D': 30, 'E': 31, 'F': 32, 'G': 33, 'H': 34, 'I': 35,
    'J': 36, 'K': 37, 'L': 38, 'M': 39, 'N': 40, 'O': 41, 'P': 42, 'Q': 43, 'R': 44,
    'S': 45, 'T': 46, 'U': 47, 'V': 48, 'W': 49, 'X': 50, 'Y': 51, 'Z': 52
    }

# Split the rucksack contents into the two compartments
rucksacks_two_compartments = []
for rucksack_content in rucksack_input:
    rucksack_content_amount = len(rucksack_content)
    rucksack = [rucksack_content[:rucksack_content_amount//2], rucksack_content[rucksack_content_amount//2:]]
    rucksacks_two_compartments.append(rucksack)
#print(rucksacks_two_compartments)

# Find repeated letters between the compartments
repeated_letters = []
for rucksack in rucksacks_two_compartments:
    repeated_letters.append((list(set(rucksack[0]) & set(rucksack[1]))[0]))
repeated_letters = list(repeated_letters)
#print(repeated_letters)

# Find the priority of the repeated letters
priority = []
for letter in repeated_letters:
    priority.append(priority_map[str(letter)])

# Sum of priorities
print(sum(priority))

## Part 2

# Find badges
badges = []
for i in range(2,len(rucksacks_two_compartments),3): # Index for every third elf/rucksack
    badges.append(list(set(rucksack_input[i]) & set(rucksack_input[i-1]) & set(rucksack_input[i-2]))[0])

# Find the priority of the badges
badge_priority = []
for badge in badges:
    badge_priority.append(priority_map[str(badge)])

# Sum of badge priorities
print(sum(badge_priority))

end = time.time()
print("Execution time: ", end - start)