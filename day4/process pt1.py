total = 0
with open("input.txt", "r") as f:
    for line in f:
        winners = line[line.find(":")+1:line.find("|")].strip().split()
        have = line[line.find("|")+1:].strip().split()
        local = 0
        for elt in have:
            if elt in winners:
                local = 1 if local == 0 else local *2
                
        total += local
print(total)