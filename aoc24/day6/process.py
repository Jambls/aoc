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
grids = []
for i,line in enumerate(grid):
    for j,elt in enumerate(line):
        newgrid = copy.deepcopy(grid)
        newgrid[i][j] = '#'
        grids.append(newgrid)
       
    
    



for newgrid in grids:
    nl = location
    nd = direction
    loclist = []
    pprint(newgrid)
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
    



xcount = []
for line in grid:
    xcount.append([1 if x == 'X' else 0 for x in line])
print(count)
