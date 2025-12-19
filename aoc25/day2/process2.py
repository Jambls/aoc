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

def checker(chunk, rest):
    # print(chunk, "and", rest)
    if rest == "":
        # print("hit")
        return 1
    elif len(rest) < len(chunk):
        return 0
    elif rest[0:len(chunk)] != chunk:
        return 0
    else:
        return checker(chunk, rest[len(chunk):])


total = 0
for id in ids:
    half = id[0:len(id)//2+1]
    patter = int(id)
    for i in range(1, len(half)):
        # print(id[:i])
        if checker(id[0:i], id[i:]):
            # print( "found patters ", patter)
            total += patter 
            break

print(total)