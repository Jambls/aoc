bas = []
bbs = []
ps = []
with open("inputsmall.txt") as f:
    for line in f:
        line = line.strip().split()
        if line:
            if line[0] == 'Prize:':
                ps.append((int(line[1].split("=")[1].strip(",")), int(line[2].split("=")[1])))
            elif line[1] == "A:":
                bas.append((int(line[2].split("+")[1].strip(",")), int(line[3].split("+")[1])))
            elif line[1] == "B:":
                bbs.append((int(line[2].split("+")[1].strip(",")), int(line[3].split("+")[1])))

total = 0
found = False
for i in range(len(bas)):
    for j in range(101):
        for k in range(101):
            if j*bas[i][0] + k*bbs[i][0] == ps[i][0] and j*bas[i][1] + k*bbs[i][1] == ps[i][1]:
                total += 3*j+k
                found = True
                break
        if found:
            break
    found = False

print(total)

