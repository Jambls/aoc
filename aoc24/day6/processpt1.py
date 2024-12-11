from pprint import pprint
grid =[]
with open("input.txt") as f:
    for line in f:
        grid.append(list(line.strip()))

location = (0,0)
for i,line in enumerate(grid):
    if "^" in line:
        location = (line.index("^"), i)
direction = (0,-1)

while (0<=location[0]<len(grid[0]) and 0 <= location[1] < len(grid)):
    
    grid[location[1]][location[0]] = "X"
    if 0<=location[1]+direction[1] < len(grid) and 0 <= location[0]+direction[0] < len(grid[0]) and '#' in grid[location[1]+direction[1]][location[0]+direction[0]]:
        direction = (0-direction[1], direction[0])
    location = (location[0]+direction[0], location[1]+direction[1])

pprint(grid)
xcount = []
for line in grid:
    xcount.append([1 if x == 'X' else 0 for x in line])
print(sum([sum(x) for x in xcount]))
