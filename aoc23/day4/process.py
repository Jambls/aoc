num_winners = []
with open("input.txt", "r") as f:
    for line in f:
        winners = line[line.find(":")+1:line.find("|")].strip().split()
        have = line[line.find("|")+1:].strip().split()
        local = 0
        for elt in have:
            if elt in winners:
                local += 1
        num_winners.append(local)

total = [1]*len(num_winners)
for i,elt in enumerate(num_winners):
    if elt > 0:
        for j in range(i+1, i+elt+1):
            total[j] +=  1 * total[i]

print(sum(total))