equations = []
with open("input.txt") as f:
    for line in f:
        equations.append([int(line.split(":")[0])] + list(map(int, list(line.strip().split())[1:])))
        
def everytotal(nums, acc):
    if len(nums) == 0:
        return [acc]
    else:
        return everytotal(nums[1:], acc*nums[0]) + everytotal(nums[1:], acc + nums[0]) + everytotal(nums[1:], int(str(acc) + str(nums[0])))
    

total = 0
for eq in equations:
    if eq[0] in everytotal(eq[2:], eq[1]):
        total += eq[0]

print(total)