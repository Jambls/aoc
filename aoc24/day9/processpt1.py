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
        return [count] * list[0]
    return [count] * list[0] + ["."] * list[1] + separate(list[2:], count +1)

grid = separate(grid)

def remove_dots(list):
    if list[-1] == ".":
        list.pop()
        remove_dots(list)

counter = 0
remove_dots(grid)
while counter < len(grid):
    if grid[counter] == ".":
        grid[counter] = grid[-1]
        grid.pop()
    counter += 1
    remove_dots(grid)

total = 0
for i, elt in enumerate(grid):
    total += i*elt

print(total)

