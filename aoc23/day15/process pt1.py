chunks = []
with open("input.txt") as f:
    chunks = f.readline().strip().split(",")

chunknums = []
for str in chunks:
    current = 0
    for c in str:
        current += ord(c)
        current *= 17
        current = current % 256
    chunknums.append(current)

print(sum(chunknums))