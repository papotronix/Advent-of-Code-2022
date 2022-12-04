import time
start = time.time()


## Part 1
section_assignment_pairs = open('Day_4/input.txt', 'r', newline=None).read().split('\n')
#print(section_assignment_pairs)

for i in range(len(section_assignment_pairs)):
    section_assignment_pairs[i] = section_assignment_pairs[i].split(',')
#print(section_assignment_pairs)

for i in range(len(section_assignment_pairs)):
    for j in range(len(section_assignment_pairs[i])):
        section_assignment_pairs[i][j] = section_assignment_pairs[i][j].split('-')
#print(section_assignment_pairs)

repeated_section_assignment_pairs = 0
overlap_section_assignment_pairs = 0
for i in range(len(section_assignment_pairs)):
    setA = set(list(range((int(section_assignment_pairs[i][0][0])),(int(section_assignment_pairs[i][0][1])+1)))) 
    setB = set(list(range((int(section_assignment_pairs[i][1][0])),(int(section_assignment_pairs[i][1][1])+1))))
    # Part 1
    if (setA | setB) == setA or (setA | setB) == setB:
        repeated_section_assignment_pairs += 1
    # Part 2
    if (setA & setB) != set() or (setA & setB) != set():
        overlap_section_assignment_pairs += 1

print(repeated_section_assignment_pairs)
print(overlap_section_assignment_pairs)


end = time.time()
print("Execution time: ", end - start)