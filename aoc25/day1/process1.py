rots = []
with open("input.txt") as f:
    for line in f:
        rots.append( (1 if line[0] == 'R' else -1) *  int(line.strip()[1:]))
        
pos = 50
zeros = 0
for line in rots:
    # print(pos, line)
    pos = (pos + line) % 100
    if pos < 0:
        pos = 100 - pos
    if pos == 0:
        zeros += 1

print(zeros)