instructions = []
with open("input.txt") as f:
    instructions = f.readline().strip().split(",")

def hash(str):
    if "-" in str:
        str = str[:-1]
    elif "=" in str:
        str = str[:-2]
    current = 0
    for c in str:
        current += ord(c)
        current *= 17
        current = current % 256
    return current

def findlens(str, box):
    if "-" in str:
        str = str[:-1]
    elif "=" in str:
        str = str[:-2]
    for i,elt in enumerate(box):
        if "-" in elt:
            if str == elt[:-1]:
                return i
        else:
            if str == elt[:-2]:
                return i
    return -1

boxes = {}
for i in range(256):
    boxes[i] = []

for instr in instructions:
    if "-" in instr:
        location = findlens(instr, boxes[hash(instr)])
        if location >= 0:
            boxes[hash(instr)].pop(location)
    else:
        location = findlens(instr, boxes[hash(instr)])
        if location >= 0:
            boxes[hash(instr)][location] = instr
        else:
            boxes[hash(instr)].append(instr)

total = 0
for key,value in boxes.items():
    for i,elt in enumerate(value):
        total += (1+key) * (1+i) * int(elt[-1])
# print(boxes)
print(total)