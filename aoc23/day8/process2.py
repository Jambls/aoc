nodes = {}
with open("input.txt") as f:
    instuctions = [0 if elt == "L" else 1 for elt in f.readline().strip()]
    f.readline()
    for line in f:
        nodes[line[0:3]] = [line[7:10], line[12:15]]

current = ""
for node in nodes:
    current = node
    for i,inst in enumerate(instuctions):
        current = nodes[current][inst]
    nodes[node].append(current)

instptr = 0
counter = 0

current = []

for node in nodes.keys():
    if node[2] == "A":
        current.append(node)

while not all(elt[2] == "Z" for elt in current):
    current = [nodes[elt][2] for elt in current]
    counter += len(instuctions)
print(counter)

