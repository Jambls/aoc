map = []
start = []
with open("input.txt") as f:
    for line in f:
        map.append([elt for elt in line.strip()])
        if "S" in line:
            start = [line.index("S"), len(map)-1]

def findnext(map, current, last):
    curx, cury = current
    lastx, lasty = last
    if map[cury][curx] == "|":
        if lasty == cury -1:
            return[curx, cury+1]
        else:
            return[curx, cury-1]
    elif map[cury][curx] == "-":
        if lastx == curx -1:
            return[curx +1, cury]
        else:
            return[curx-1, cury]
    elif map[cury][curx] == "L":
        if lasty == cury -1:
            return[curx +1, cury]
        else:
            return[curx, cury-1]
    elif map[cury][curx] == "J":
        if lasty == cury -1:
            return[curx -1, cury]
        else:
            return[curx, cury-1]
    elif map[cury][curx] == "7":
        if lastx == curx -1:
            return[curx, cury+1]
        else:
            return[curx-1, cury]
    elif map[cury][curx] == "F":
        if lastx == curx +1:
            return[curx, cury+1]
        else:
            return[curx +1, cury]
    else:
        raise Exception("findnext has invalid current location")


if map[start[1]-1][start[0]] == "|" or map[start[1]-1][start[0]] == "7" or map[start[1]-1][start[0]] == "F":
    current = [start[0], start[1]-1]
    last = start
elif map[start[1]][start[0]+1] == "-" or map[start[1]][start[0]+1] == "J" or map[start[1]][start[0]+1] == "7":
    current = [start[0]+1, start[1]]
    last = start
elif map[start[1]+1][start[0]] == "|" or map[start[1]+1][start[0]] == "L" or map[start[1]+1][start[0]] == "J":
    current = [start[0], start[1]+1]
    last = start
else:
    raise Exception("could not find valid move from start")

count = 1
while map[current[1]][current[0]] != "S":

    next = findnext(map, current, last)
    last = current
    current = next
    count += 1

print(count/2)