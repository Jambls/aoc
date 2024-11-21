nodes = {}
with open("input.txt") as f:
    instuctions = [0 if elt == "L" else 1 for elt in f.readline().strip()]
    f.readline()
    for line in f:
        nodes[line[0:3]] = [line[7:10], line[12:15]]

current = ""

instptr = 0
counter = 0

nodetoz = {}

for node in nodes:
    nodetoz[node] = []
    current = node
    for i,inst in enumerate(instuctions):
        if current[2] == "Z":
            nodetoz[node].append(i)
        current = nodes[current][inst]
    nodes[node].append(current)

counter = 0

current = []

for node in nodes.keys():
    if node[2] == "A":
        current.append(node)
while not set.intersection(*[set(nodetoz[elt]) for elt in current]):
    current = [nodes[elt][2] for elt in current]
    counter += len(instuctions)
print(counter)
print(set.intersection(*[set(nodetoz[elt]) for elt in current]))
print(counter + min(set.intersection(*[set(nodetoz[elt]) for elt in current])))