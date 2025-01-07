grid = []
with open("input.txt") as f:
    for line in f:
        line = list(line.strip())
        grid.append([x for x in line])

def find(current, prev, hfences, vfences):
    letter = grid[current[0]][current[1]]
    prev.append(current)
    edges = 0
    if current[0]-1 >= 0 and grid[current[0]-1][current[1]] == letter and [current[0]-1,current[1]] not in prev:
        edges += find([current[0]-1, current[1]], prev, hfences, vfences)
    elif [current[0]-1,current[1]] not in prev:
        hfences[current[0]*2][current[1]] = "-"
        edges +=1
    if current[0]+1 < len(grid) and grid[current[0]+1][current[1]] == letter and [current[0]+1,current[1]] not in prev:
        edges += find([current[0]+1, current[1]], prev, hfences, vfences)
    elif [current[0]+1,current[1]] not in prev:
        hfences[current[0]*2+1][current[1]] = "-"
        edges +=1
    if current[1]-1 >= 0 and grid[current[0]][current[1]-1] == letter and [current[0],current[1]-1] not in prev:
        edges += find([current[0], current[1]-1], prev, hfences, vfences)
    elif [current[0],current[1]-1] not in prev:
        edges +=1
        vfences[current[1]*2][current[0]] = "-"
    if current[1]+1 < len(grid[0]) and grid[current[0]][current[1]+1] == letter and [current[0],current[1]+1] not in prev:
        edges += find([current[0], current[1]+1], prev, hfences, vfences)
    elif [current[0],current[1]+1] not in prev:
        edges +=1
        vfences[current[1]*2+1][current[0]] = "-"

    return edges


total = 0
visited = []
for i,line in enumerate(grid):
    for j,elt in enumerate(line):
        if [i, j] not in visited:
            hfences = [["." for _ in range(len(grid[0])+1)] for _ in range((len(grid)+1)*2)]
            vfences = [["." for _ in range(len(grid)+1)] for _ in range((len(grid[0])+1)*2)]
            points = []
            find([i,j], points, hfences, vfences)
            perimiter = 0
            for k, row in enumerate(hfences):
                for l, elt in enumerate(row):
                    if elt == "-" and ((l +1 < len(row) and row[l+1] == ".") or l == len(row) -1):
                        perimiter += 1
            for k, row in enumerate(vfences):
                for l, elt in enumerate(row):
                    if elt == "-" and ((l +1 < len(row) and row[l+1] == ".") or l == len(row) -1):
                        perimiter += 1


            total += perimiter * len(points)
            visited += points



print(total)