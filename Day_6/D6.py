import time
start = time.time()

datastream = open('Day_6/input.txt', 'r', newline=None).read()#.split('\n')
#print(datastream)

datastream = ''.join([datastream]) 

## Part 1
for i in range(len(datastream)-4):
    tetrad = list(datastream[i:i+4])
    repeat = False
    for j in range(0,4):
        triad = tetrad.copy()
        triad.pop(j)
        if tetrad[j] in triad:
            repeat = True
            break 
    if repeat == False:
        print(i+4)
        break
    
## Part 2
for i in range(len(datastream)-14):
    fourteen_chars = list(datastream[i:i+14])
    repeat = False
    for j in range(0,14):
        thirtheen_chars = fourteen_chars.copy()
        thirtheen_chars.pop(j)
        if fourteen_chars[j] in thirtheen_chars:
            repeat = True
            break 
    if repeat == False:
        print(i+14)
        break


end = time.time()
print("Execution time: ", end - start)