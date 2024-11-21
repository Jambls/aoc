seeds = []
maps = [{} for _ in range(7)]
with open("input.txt", "r") as f:
    seeds = list(map(int, f.readline()[7:].strip().split()))
    seeds = [[seeds[i],seeds[i+1]] for i in range(0,len(seeds),2)]
    line = f.readline()
    for i in range(7):
        f.readline()
        while (any(map(str.isdigit,line := f.readline()))):
            splitline = list(map(int, line.strip().split()))
            maps[i][splitline[1]] = [splitline[2],splitline[0]]

total = 0
for i in range(len(seeds)):
    total += seeds[i][1]
print(total)