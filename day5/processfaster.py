seeds = []
maps = [{} for _ in range(7)]
with open("inputmark.txt", "r") as f:
    seeds = list(map(int, f.readline()[7:].strip().split()))
    seeds = [[seeds[i],seeds[i+1]] for i in range(0,len(seeds),2)]
    line = f.readline()
    for i in range(7):
        f.readline()
        while (any(map(str.isdigit,line := f.readline()))):
            splitline = list(map(int, line.strip().split()))
            # input range start : [range, output range start]
            maps[i][splitline[1]] = [splitline[2],splitline[0]]

for i in range(600279879):
    temp = i
    for map in maps[::-1]:
        for key,value in map.items():
            if value[1] <= temp < value[1] + value[0]:
                temp = temp - value[1] + key
                break
    # check if in a valid input seed
    for seed in seeds:
        if seed[0] <= temp < seed[0]+seed[1]:
            tempseed = temp
            for map in maps:
                for key,value in map.items():
                    if key <= tempseed < key+value[0]:
                        tempseed = tempseed-key + value[1]
                        break
              
            if tempseed == i:        
                print(i)
                quit()
    
