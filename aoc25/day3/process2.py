banks = []
with open("input.txt") as f:
    for line in f:
        banks.append(line.strip())

# print(banks)

def find_highest(block):
    if block == "":
        return ("0", "")
    next_num, next_block = find_highest(block[1:])
    if int(next_num) > int(block [0]):
        return (next_num, next_block)
    else:
        return (block[0], block[1:])
    
total = 0
for bank in banks:
    number = ""
    block = bank[:-11]
    # print("bank", bank)
    
    for j in range(11, -1, -1):
        # print("block", block)
        num, ret_block = find_highest(block)
        number += num
        block = ret_block + bank[-j]
        # print(number)
    total += int(number)

    # num1, rest = find_highest(bank)
    # if rest == "":
    #     num1, rest = find_highest(bank[:-1])
    #     rest += bank[-1]
    # num2, rest = find_highest(rest)
    # total += int(num1+num2)

print(total)