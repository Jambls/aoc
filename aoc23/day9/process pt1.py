sequences = []
with open("input.txt") as f:
    for line in f:
        sequences.append([int(elt) for elt in line.strip().split()])

def calc(lst):
    if all(elt == 0 for elt in lst):
        return 0
    newlist = []
    for i in range(len(lst)-1):
        newlist.append(lst[i+1] - lst[i])
    return newlist[-1] + calc(newlist)

total = 0
for elt in sequences:
    total += elt[-1] + calc(elt)

print(total)