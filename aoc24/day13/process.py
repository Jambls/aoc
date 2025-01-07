bas = []
bbs = []
ps = []
with open("input.txt") as f:
    for line in f:
        line = line.strip().split()
        if line:
            if line[0] == 'Prize:':
                ps.append((10000000000000+int(line[1].split("=")[1].strip(",")), 10000000000000+int(line[2].split("=")[1])))
            elif line[1] == "A:":
                bas.append((int(line[2].split("+")[1].strip(",")), int(line[3].split("+")[1])))
            elif line[1] == "B:":
                bbs.append((int(line[2].split("+")[1].strip(",")), int(line[3].split("+")[1])))

total = 0
for i in range(len(bas)):
    eqn1 = [bas[i][0], bbs[i][0], ps[i][0]]
    eqn2 = [bas[i][1], bbs[i][1], ps[i][1]]
    eqn3 = [elt * eqn2[0] for elt in eqn1]
    eqn4 = [elt * eqn1[0] for elt in eqn2]
    b = ((eqn3[2] - eqn4[2])*1.0)/(eqn3[1] - eqn4[1])
    a = ((eqn1[2] - eqn1[1]*b)*1.0)/eqn1[0]
    if int(a) == a and int(b) == b and a > 0 and b > 0:
        total += int(a) *3+ int(b)
    

print(total)

