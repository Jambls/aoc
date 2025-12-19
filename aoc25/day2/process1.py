input = ""
with open("input.txt") as f:
    for line in f:
        input = line.strip()

ranges = input.split(",")
ids = []
for ran in ranges:
    start, end = map(int, ran.split("-"))
    for i in range(start, end+1):
        ids.append(str(i))

total = 0
for id in ids:
    if id[0:len(id)//2] == id[len(id)//2:]:
        # print(id)
        total += int(id)

print(total)