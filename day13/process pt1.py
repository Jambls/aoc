map = []
maps = []
with open("input.txt") as f:
    for line in f:
        
        if line == "\n":
            maps.append(map)
            map = []
        else:
            map.append([elt for elt in line.strip()])
maps.append(map)

reflect_vertical = []
reflect_horizontal = []

for map in maps:
    # print(map)
    for i in range(1,len(map[0])):
        reflect = True
        start = i - (len(map[0]) - i)
        start = 0 if start < 0 else start
        stop = 2*i if 2*i < len(map[0]) else len(map[0])
        for line in map:
            if line[start:i] != line[i:stop][::-1]:
                reflect = False
                # print(line[start:i] , line[i:stop][::-1], start, i, stop)
                break
        
        if reflect:
            reflect_vertical.append(i)

    for i in range(1,len(map)):
        start = i - (len(map) - i)
        start = 0 if start < 0 else start
        stop = 2*i if 2*i < len(map) else len(map)
        # print(map[start:i], map[i:stop][::-1], start, i, stop)
        if map[start:i] == map[i:stop][::-1]:
            reflect_horizontal.append(i)


print(reflect_horizontal)
print(reflect_vertical)
print(sum(reflect_vertical) + sum(reflect_horizontal)*100)