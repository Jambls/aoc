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

minimum = 2**32
for i in range(len(seeds)):
    for seed in range(seeds[i][0], seeds[i][0] + seeds[i][1]):
        tempseed = seed
        for map in maps:
            for key,value in map.items():
                if key <= tempseed < key+value[0]:
                    tempseed = tempseed-key + value[1]
                    break
        minimum = minimum if tempseed > minimum else tempseed
                    
print(minimum)