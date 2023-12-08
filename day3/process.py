array = []
total = 0
found = 0

def findnumber(arr, x, y):
    if arr[y][x-1].isdigit():
        return findnumber(arr,x-1,y)
    else:
        global found
        found += 1
        return collectnumber(arr, x,y)

def collectnumber(arr, x, y, num = 0):
    num += int(arr[y][x])
    if arr[y][x+1].isdigit():
        return collectnumber(arr,x+1,y, 10* num)
    return num

with open("input.txt", "r") as f:
    for line in f:
        array.append("." + line.strip() + ".")

array.insert(0, "."*len(array[0]))
array.append("."*len(array[0]))

for y in range(len(array)):
    for x in range(len(array[0])):
        if array[y][x] == "*":
            temp = 1
            found = 0
            if array[y][x-1].isdigit():
                temp = temp * findnumber(array, x-1, y)
            if array[y][x+1].isdigit():
                temp = temp * findnumber(array, x+1, y)
            if array[y-1][x].isdigit():
                temp = temp * findnumber(array, x, y-1)
            else:
                if array[y-1][x-1].isdigit():
                    temp = temp * findnumber(array, x-1, y-1)
                if array[y-1][x+1].isdigit():
                    temp = temp * findnumber(array, x+1, y-1)
            if array[y+1][x].isdigit():
                temp = temp * findnumber(array, x, y+1)
            else:
                if array[y+1][x-1].isdigit():
                    temp = temp * findnumber(array, x-1, y+1)
                if array[y+1][x+1].isdigit():
                    temp = temp * findnumber(array, x+1, y+1)

            if found == 2:
                total += temp

print(total)