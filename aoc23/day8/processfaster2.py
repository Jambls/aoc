import math
nodes = {}
with open("input.txt") as f:
    instuctions = [0 if elt == "L" else 1 for elt in f.readline().strip()]
    f.readline()
    for line in f:
        nodes[line[0:3]] = [line[7:10], line[12:15]]


instptr = 0
counter = 0

starters = []

for node in nodes:
    if node[2] == "A":
        starters.append(node)

distances = []

for i,current in enumerate(starters):
    counter = 0
    instptr = 0
    while current[2] != "Z":
        current = nodes[current][instuctions[instptr]] 
        counter += 1
        instptr = (instptr + 1) % len(instuctions)
    distances.append(counter)


print(math.lcm(*distances))