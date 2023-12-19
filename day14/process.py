import copy
map = []
with open("input.txt") as f:
    for line in f:
        map.append( [elt for elt in line.strip()])

lastmap = []
count = 0
while count < 1000000000 and not map in lastmap:
    lastmap.append(copy.deepcopy(map))
    
    for _ in range(4):
        for i in range(len(map)):
            for j in range(len(map[0])):
                obj = map[i][j]
                newi = i
                if obj == "O":
                    while newi > 0 and map[newi-1][j] == ".":
                        newi = newi -1
                    map[i][j], map[newi][j] = map[newi][j], map[i][j]
        
        map = list(zip(*reversed(map)))
        map = [list(elt) for elt in map]
    
    count += 1



start = lastmap.index(map)
loop = len(lastmap) - start
final_i = (1000000000 - start) % loop + start
print(final_i)
total = 0
for i,line in enumerate(lastmap[final_i]):
    total += line.count("O") * (len(map) - i)
print(total)