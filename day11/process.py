import numpy as np

map = []
with open("input.txt") as f:
    for line in f:
        map.append([elt for elt in line.strip()])

nmap = np.array(map)
galaxies = []
xgaps = []
ygaps = []

for i in reversed(range(np.shape(nmap)[0])):
    if not "#" in nmap[i]:
        ygaps.append(i)
    


for i in reversed(range(np.shape(nmap)[1])):
    if not "#" in nmap[:,i]:
        xgaps.append(i)

total = 0
for i in range(np.shape(nmap)[0]):
    for j, elt in enumerate(nmap[i]):
        if elt == "#":
            galaxies.append([j,i])
    
for i in range(len(galaxies)-1):
    for j in range(i+1, i + len(galaxies[i+1:])+1):
        total += abs(galaxies[i][0] - galaxies[j][0]) + abs(galaxies[i][1] - galaxies[j][1])
        startx = min([galaxies[i][0], galaxies[j][0]])
        finx = max([galaxies[i][0], galaxies[j][0]])
        starty = min([galaxies[i][1], galaxies[j][1]])
        finy = max([galaxies[i][1], galaxies[j][1]])
        # print(i, " ", j, " ", startx, starty)
        for k in range(startx, finx):
            if k in xgaps:
                total += 1000000-1
        for k in range(starty, finy):
            if k in ygaps:
                total += 1000000-1



# print(nmap)
# print(galaxies)
print(total)