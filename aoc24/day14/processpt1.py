pos = []
vel = []
with open("input.txt") as f:
    for line in f:
        line = line.strip().split()
        positions = line[0].split("=")[1]
        velocities = line[1].split("=")[1]
        pos.append(map(int, positions.split(",")))
        vel.append(map(int, velocities.split(",")))

for i in range(len(pos)):
    pos[i] = [(pos[i][0] + 100 * vel[i][0])% 101, (pos[i][1] + 100 * vel[i][1])% 103]

print(pos)

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