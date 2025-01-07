import sys
sys.setrecursionlimit(25000)

grid = []
with open("input.txt") as f:
    for line in f:
        grid=(list(line.strip()))
grid = [int(x) for x in grid]


def separate(list, count = 0):
    if len(list) == 0:
        return []
    if len(list) == 1:
        return [(count , list[0])]
    return [(count , list[0])] + [("." , list[1])] + separate(list[2:], count +1)

grid = separate(grid)

def findspace(grid, size):
    index = 0
    while(index < len(grid)):
        if grid[index][0] == "." and grid[index][1] >= size:
            return index
        index += 1

i = len(grid) -1
while i >=0:
    if grid[i][0] != ".":
        space_index = findspace(grid, grid[i][1])
        if not space_index or space_index >= i:
            i -= 1
            continue
        space_size = grid[space_index][1]
        if space_size == grid[i][1]:
            grid[space_index] = grid[i]
            # i think I can just leave this as a fragmented line of dots as I should never move stuff right
            grid[i] = (".", grid[i][1])
        else:
            remaining_size = space_size - grid[i][1]
            grid[space_index] = grid[i]
            grid.insert(space_index+1, (".", remaining_size))
            i += 1
            grid[i] = (".", grid[i][1])
    i -= 1

print(grid)


total = 0
i = 0
for elt in grid:
    if elt[0] != ".":
        for j in range(elt[1]):
            total += elt[0]*i
            i += 1
    else:
        i += elt[1]

print(total)

