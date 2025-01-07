grid = []
with open("input.txt") as f:
    for line in f:
        line = list(line.strip().split())
        grid.append([int(x) for x in line])

data = {x:1 for x in grid[0]}

def step(number):
    if number == 0:
        return [1]
    elif len(str(number)) %2 == 0:
        return [int(str(number)[:len(str(number))/2]), int(str(number)[len(str(number))/2:])]
    else:
        return [number * 2024]
    
newdata = {}
for i in range(75):
    for key in data:
        next = step(key)
        for elt in next:
            if elt in newdata:
                newdata[elt]+=data[key]
            else:
                newdata[elt] = data[key]
    data = newdata
    newdata = {}

total = 0
for key in data:
    total += data[key]

print(total)
print(data)