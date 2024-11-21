seeds = []
maps = [{} for _ in range(7)]
with open("input.txt", "r") as f:
    seeds = list(map(int, f.readline()[7:].strip().split()))
    line = f.readline()
    for i in range(7):
        f.readline()
        while (any(map(str.isdigit,line := f.readline()))):
            splitline = list(map(int, line.strip().split()))
            maps[i][splitline[1]] = [splitline[2],splitline[0]]

for i,seed in enumerate(seeds):
    for map in maps:
        for key,value in map.items():
            if key <= seeds[i] < key+value[0]:
                seeds[i] = seeds[i]-key + value[1]
                break
                
print(seeds)