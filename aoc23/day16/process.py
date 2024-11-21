import sys
sys.setrecursionlimit(20000)
import copy

map = []
with open("input.txt") as f:
    for line in f:
        map.append([elt for elt in line.strip()])

energized_base = []
for _ in range(len(map)):
    energized_base.append(["." for _ in map[0]])

visited = []

def nxt(map, current, last):
    if (current, last) in visited:
        return
    visited.append((current,last))
    curx, cury = current
    lastx, lasty = last
    if curx < 0 or curx >= len(map[0]):
        return
    elif cury < 0 or cury >= len(map):
        return
    if energized[cury][curx] == ".":
        energized[cury][curx] = "#"
    if map[cury][curx] == ".":
        nxt(map, (curx + (curx-lastx), cury + (cury-lasty)), current)
    elif map[cury][curx] == "/":
        nxt(map, (curx - (cury-lasty), cury - (curx-lastx)), current)
    elif map[cury][curx] == "\\":
        nxt(map, (curx + (cury-lasty), cury + (curx-lastx)), current)
    elif map[cury][curx] == "|":
        if curx == lastx:
            nxt(map, (curx + (curx-lastx), cury + (cury-lasty)), current)
        else:
            nxt(map, (curx, cury + 1), current)
            nxt(map, (curx, cury - 1), current)
    elif map[cury][curx] == "-":
        if cury == lasty:
            nxt(map, (curx + (curx-lastx), cury + (cury-lasty)), current)
        else:
            nxt(map, (curx + 1, cury), current)
            nxt(map, (curx - 1, cury), current)
    else:
        raise Exception("unexpected input")

total = 0
for i,_ in enumerate(map):
    energized = copy.deepcopy(energized_base)
    visited = []
    temp = 0
    nxt(map, [0,i], [-1, i])
    for line in energized:
        temp += line.count("#")
    if temp > total:
        total = temp
    energized = copy.deepcopy(energized_base)
    visited = []
    temp = 0
    nxt(map, [len(map[0])-1,i], [len(map[0]), i])
    for line in energized:
        temp += line.count("#")
    if temp > total:
        total = temp

for i,_ in enumerate(map[0]):
    energized = copy.deepcopy(energized_base)
    visited = []
    temp = 0
    nxt(map, [i,0], [i, -1])
    for line in energized:
        temp += line.count("#")
    if temp > total:
        total = temp
    energized = copy.deepcopy(energized_base)
    visited = []
    temp = 0
    nxt(map, [i,len(map)-1], [i,len(map)])
    for line in energized:
        temp += line.count("#")
    if temp > total:
        total = temp



print(total)