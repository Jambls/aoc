grid = []
with open("input.txt", "r") as f:
    for line in f: grid.append(line.strip())

crosses = []

for i in range(len(grid)-2):
    for j in range(len(grid[0])-2):
        crosses.append(grid [i+1][j+1] + grid[i][j] + grid[i][j+2] + grid[i+2][j] + grid[i+2][j+2])

def checkcrosses(cross):
    if cross == "AMSMS" or cross == "AMMSS" or cross == "ASMSM" or cross == "ASSMM":
        return 1
    else:
        return 0
    
print(sum(map(checkcrosses, crosses)))
