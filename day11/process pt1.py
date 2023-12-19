import numpy as np

map = []
with open("inputsmall.txt") as f:
    for line in f:
        map.append([elt for elt in line.strip()])

nmap = np.array(map)
galaxies = []

# for i in reversed(range(np.shape(nmap)[0])):
#     if not "#" in nmap[i]:
#         nmap = np.insert(nmap, i,nmap[i], 0)
    


# for i in reversed(range(np.shape(nmap)[1])):
#     if not "#" in nmap[:,i]:
#         nmap = np.insert(nmap, i,nmap[:,i],  1)

total = 0
for i in range(np.shape(nmap)[0]):
    for j, elt in enumerate(nmap[i]):
        if elt == "#":
            galaxies.append([j,i])
    
for i in range(len(galaxies)-1):
    for j in range(i+1, i + len(galaxies[i+1:])+1):
        total += abs(galaxies[i][0] - galaxies[j][0]) + abs(galaxies[i][1] - galaxies[j][1])
        # print(i, " ", j, " ", galaxies[i], " ", galaxies[j])

# print(nmap)
# print(galaxies)
print(total)
# print( abs(galaxies[7][0] - galaxies[8][0]) + abs(galaxies[7][1] - galaxies[8][1]))