import re

modified = []
results = []

with open("input.txt", "r") as f:
    for line in f:
        results.append(re.search("\d|one|two|three|four|five|six|seven|eight|nine", line.strip())[0] + re.search("\d|eno|owt|eerht|ruof|evif|xis|neves|thgie|enin", line.strip()[::-1])[0][::-1])
        
for line in results:
    modified.append(line.replace("one", "1").replace("two", "2").replace("three", "3").replace("four","4").replace("five", "5").replace("six", "6").replace("seven","7").replace("eight","8").replace("nine","9"))

intresults = [int(elt) for elt in modified]

print(sum(intresults))