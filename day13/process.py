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
        errors = 0
        start = i - (len(map[0]) - i)
        start = 0 if start < 0 else start
        stop = 2*i if 2*i < len(map[0]) else len(map[0])
        for line in map:
            for j in range(start, i):
                if line[j] != line[i+(i-j)-1]:
                    errors +=1
                # print(line[start:i] , line[i:stop][::-1], start, i, stop)
                
        
        if errors == 1:
            reflect_vertical.append(i)

    for i in range(1,len(map)):
        start = i - (len(map) - i)
        start = 0 if start < 0 else start
        stop = 2*i if 2*i < len(map) else len(map)
        errors = 0
        for j in range(start, i):
            for k in range(len(map[j])): 
                # print(i, j, k, i+(i-j)-1)
                if map[j][k] != map[i+(i-j)-1][k]:
                    errors += 1

        if errors == 1:    
            reflect_horizontal.append(i)


print(reflect_horizontal)
print(reflect_vertical)
print(sum(reflect_vertical) + sum(reflect_horizontal)*100)