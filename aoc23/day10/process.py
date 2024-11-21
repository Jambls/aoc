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

nearstart = []
if map[start[1]-1][start[0]] == "|" or map[start[1]-1][start[0]] == "7" or map[start[1]-1][start[0]] == "F":
    current = [start[0], start[1]-1]
    last = start
    nearstart.append("up")
if map[start[1]][start[0]+1] == "-" or map[start[1]][start[0]+1] == "J" or map[start[1]][start[0]+1] == "7":
    current = [start[0]+1, start[1]]
    last = start
    nearstart.append("right")
if map[start[1]+1][start[0]] == "|" or map[start[1]+1][start[0]] == "L" or map[start[1]+1][start[0]] == "J":
    current = [start[0], start[1]+1]
    last = start
    nearstart.append("down")
if map[start[1]][start[0]-1] == "-" or map[start[1]][start[0]-1] == "L" or map[start[1]][start[0]-1] == "F":
    current = [start[0], start[1]+1]
    last = start
    nearstart.append("left")


cleanmap = [["." for x in line]for line in map]
startchar = "S"

if "up" in nearstart and "down" in nearstart:
    startchar = "|"
elif "left" in nearstart and "right" in nearstart:
    startchar = "-"
elif "up" in nearstart and "right" in nearstart:
    startchar = "L"
elif "left" in nearstart and "up" in nearstart:
    startchar = "J"
elif "left" in nearstart and "down" in nearstart:
    startchar = "7"
elif "down" in nearstart and "right" in nearstart:
    startchar = "F"

cleanmap[start[1]][start[0]] = startchar


while map[current[1]][current[0]] != "S":
    cleanmap[current[1]][current[0]] = map[current[1]][current[0]]
    next = findnext(map, current, last)
    last = current
    current = next
    
inside = False
last = "|"
count = 0

for line in cleanmap:
    for elt in line:
        if elt == "." and inside:
            count += 1
        elif elt == "|":
            inside = not inside
        elif elt == "F" or elt == "L":
            last = elt
        elif elt == "J":
            if last == "F":
                inside = not inside
        elif elt == "7":
            if last == "L":
                inside = not inside
    if inside != False:
        raise Exception("was not outside the circuit by the end of the line")


print(count)
