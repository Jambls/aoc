
grid = []
with open("input.txt") as f:
    for line in f:
        line = list(line.strip())
        grid.append([int(x) for x in line])

trailheads = {}
for i, line in enumerate(grid):
    for j, elt in enumerate(line):
        if elt == 0:
            trailheads[(i, j)] = []

def find_trails(grid, y, x):
    if grid[y][x] == 9:
        return [(y,x)]
    trails = []
    current = grid[y][x]
    if 0 <= y-1 and grid[y-1][x] == current+1:
        trails += find_trails(grid, y-1, x)
    if y +1 < len(grid) and grid[y+1][x] == current+1:
        trails += find_trails(grid, y+1, x)
    if 0 <= x-1 and grid[y][x-1] == current+1:
        trails += find_trails(grid, y, x-1)
    if x +1 < len(grid[0]) and grid[y][x+1] == current+1:
        trails += find_trails(grid, y, x+1)

    return trails

total = 0
for key in trailheads:
    total += len(find_trails(grid, key[0], key[1]))
print(total)