import re

array = []
total = 0

def nearcheck(arr,x,y):
    if columncheck(arr, x-1, y):
        return True
    elif columncheck(arr, x, y):
        return True
    elif arr[y][x+1].isdigit():
        return nearcheck(arr, x+1, y)
    elif columncheck(arr, x+1, y):
        return True
    else:
        return False

def columncheck(arr,x,y):
    if ispunct(arr[y-1][x]) or ispunct(arr[y][x]) or ispunct(arr[y+1][x]):
        return True
    else:
        return False

def ispunct(item):
    if item.isdigit():
        return False
    elif item == ".":
        return False
    else: 
        return True

with open("input.txt", "r") as f:

    for line in f:
        array.append("." + line.strip() + ".")

array.insert(0, "."*len(array[0]))
array.append("."*len(array[0]))

x = 0
y = 0


while y < len(array):
    while x < len(array[0]):
        local = array[y][x]
        if local.isdigit():
            if nearcheck(array, x,y):
                while array[y][x+1].isdigit():
                    x+=1
                    local += array[y][x]
                    
                total += int(local)
                #print(local)

        x +=1
    x = 0
    y +=1

print(total)

