map = []
with open("inputsmall.txt") as f:
    for line in f:
        map.append( [elt for elt in line.strip()])


count = 0
while count < 1000000000:
    for i in range(4):
        for i in range(len(map)):
            for j in range(len(map[0])):
                obj = map[i][j]
                newi = i
                if obj == "O":
                    while newi > 0 and map[newi-1][j] == ".":
                        newi = newi -1
                map[i][j], map[newi][j] = map[newi][j], map[i][j]
        
        map = [list(elt) for elt in zip(*reversed(map))]
        
    count += 1
# for line in map:
#     print(line)


total = 0
for i,line in enumerate(map):
    total += line.count("O") * (len(map) - i)
print(count)
print(total)