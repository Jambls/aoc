rots = []
with open("small_input.txt") as f:
    for line in f:
        rots.append( (1 if line[0] == 'R' else -1) *  int(line.strip()[1:]))
        
pos = 50
zeros = 0
for line in rots:
    print(pos, "+", line, "=", pos + line)
    if pos == 0 and line < 0 and line % 100 != 0:
        zeros -= 1
    pos = pos + line
    if pos >= 100:
        while pos >= 100:
            pos = pos - 100
            zeros +=1
    # elif pos == 100:
    #     pos = 0
    elif pos < 0:
        while pos < 0:
            pos = pos + 100
            zeros += 1
    elif pos == 0:
        zeros += 1
    print(zeros)
        
    # print(pos, line)
    # pos = pos + line
    # print(pos, "a")
    # if pos == 0:
    #     zeros += 1
    #     print("stop")
    # else:
    #     while pos >= 100:
    #         pos = pos - 100
    #         zeros +=1
    #         print("big")
    #     while pos < 0:
    #         pos = pos + 100
    #         zeros += 1
    #         print("small")
    # # if pos < 0:
    # #     pos = 100 + pos
    # #     print("under")
    

print(zeros)
# 6225 too low
# 6273 too high
# 6130 too low