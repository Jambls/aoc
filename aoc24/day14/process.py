pos = []
vel = []
with open("input.txt") as f:
    for line in f:
        line = line.strip().split()
        positions = line[0].split("=")[1]
        velocities = line[1].split("=")[1]
        pos.append(tuple(map(int, positions.split(","))))
        vel.append(tuple(map(int, velocities.split(","))))

neighbours = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
counter = 0
found = False
while set(pos) != pos and counter < 10403 and not found:
    for i in range(len(pos)):
        pos[i] = tuple([(pos[i][0] + vel[i][0])% 101, (pos[i][1] + vel[i][1])% 103])
    counter += 1
    for elt in pos:
        ncount = 0
        for adj in neighbours:
            if (elt[0] + adj[0], elt[1] + adj[1]) in pos:
                ncount += 1

        if ncount == 8:
            found = True


print(counter)

quads = [0,0,0,0]
for elt in pos:
    if elt[0] < 50 and elt[1] < 51:
        quads[0] += 1
    elif elt[0] > 50 and elt[1] < 51:
        quads[1] += 1
    elif elt[0] < 50 and elt[1] > 51:
        quads[2] += 1
    elif elt[1] > 50 and elt[1] > 51:
        quads[3] += 1
print(quads)
print(quads[0] * quads[1] * quads[2] * quads[3])