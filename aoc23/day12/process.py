condition = []
damaged = []
with open("inputsmall.txt") as f:
    for line in f:
        condition.append(line.split()[0])
        damaged.append(line.strip().split()[1].split(","))

print(condition)
print(damaged)
