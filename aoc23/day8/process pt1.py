nodes = {}
with open("input.txt") as f:
    instuctions = [0 if elt == "L" else 1 for elt in f.readline().strip()]
    f.readline()
    for line in f:
        nodes[line[0:3]] = [line[7:10], line[12:15]]

current = "AAA"

instptr = 0
counter = 0


while current != "ZZZ":
    current = nodes[current][instuctions[instptr]] 
    counter += 1
    instptr = (instptr + 1) % len(instuctions)

print(counter)