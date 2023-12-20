import sys
sys.setrecursionlimit(20000)

map = []
with open("input.txt") as f:
    for line in f:
        map.append([elt for elt in line.strip()])

energized = []
for _ in range(len(map)):
    energized.append(["." for _ in map[0]])

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

nxt(map, [0,0], [-1, 0])
total = 0
for line in energized:
    total += line.count("#")

print(total)