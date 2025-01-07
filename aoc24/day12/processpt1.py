grid = []
with open("input.txt") as f:
    for line in f:
        line = list(line.strip())
        grid.append([x for x in line])

def find(current, prev):
    letter = grid[current[0]][current[1]]
    prev.append(current)
    edges = 0
    if current[0]-1 >= 0 and grid[current[0]-1][current[1]] == letter and [current[0]-1,current[1]] not in prev:
        edges += find([current[0]-1, current[1]], prev)
    elif [current[0]-1,current[1]] not in prev:
        edges +=1
    if current[0]+1 < len(grid) and grid[current[0]+1][current[1]] == letter and [current[0]+1,current[1]] not in prev:
        edges += find([current[0]+1, current[1]], prev)
    elif [current[0]+1,current[1]] not in prev:
        edges +=1
    if current[1]-1 >= 0 and grid[current[0]][current[1]-1] == letter and [current[0],current[1]-1] not in prev:
        edges += find([current[0], current[1]-1], prev)
    elif [current[0],current[1]-1] not in prev:
        edges +=1
    if current[1]+1 < len(grid[0]) and grid[current[0]][current[1]+1] == letter and [current[0],current[1]+1] not in prev:
        edges += find([current[0], current[1]+1], prev)
    elif [current[0],current[1]+1] not in prev:
        edges +=1

    return edges


total = 0
visited = []
for i,line in enumerate(grid):
    for j,elt in enumerate(line):
        if [i, j] not in visited:
            points = []
            perimiter = find([i,j], points)
            total += perimiter * len(points)
            visited += points



print(total)