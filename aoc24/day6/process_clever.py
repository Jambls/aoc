from pprint import pprint
import copy
grid =[]
with open("input.txt") as f:
    for line in f:
        grid.append(list(line.strip()))

location = (0,0)
for i,line in enumerate(grid):
    if "^" in line:
        location = (line.index("^"), i)
direction = (0,-1)
count = 0
while (0<=location[0]+direction[0]<len(grid[0]) and 0 <= location[1]+direction[1] < len(grid)):
    
    newgrid = copy.deepcopy(grid)
    newgrid[location[1]+direction[1]][location[0]+direction[0]] = '#'
    nl = location
    nd = direction
    loclist = []
    while (0<=nl[0]<len(grid[0]) and 0 <= nl[1] < len(grid)):
        loclist.append((nl, nd))
        if 0<=nl[1]+nd[1] < len(grid) and 0 <= nl[0]+nd[0] < len(grid[0]) and '#' in newgrid[nl[1]+nd[1]][nl[0]+nd[0]]:
            nd = (0-nd[1], nd[0])
        nl = (nl[0]+nd[0], nl[1]+nd[1])
        if (nl,nd) in loclist:
            count +=1
            # pprint(newgrid)
            # print()
            break
    
    if 0<=location[1]+direction[1] < len(grid) and 0 <= location[0]+direction[0] < len(grid[0]) and '#' in grid[location[1]+direction[1]][location[0]+direction[0]]:
        direction = (0-direction[1], direction[0])
    location = (location[0]+direction[0], location[1]+direction[1])


xcount = []
for line in grid:
    xcount.append([1 if x == 'X' else 0 for x in line])
print(count)
