data_in =[]
with open("input.txt") as f:
    data_in = f.readlines()

split_location = data_in.index("\n")
rules_in = data_in[0:split_location]
pages_in = data_in[split_location+1:]
pages_list = [list(map(int, s.strip().split(','))) for s in pages_in]
rules = {}
for elt in rules_in:
    before, after = elt.strip().split("|")
    before = int(before)
    if before in rules:
        rules[before].append(int(after))
    else:
        rules[before] = [int(after)]

def middle_elt(lst):
    if len(lst) <= 2:
        return lst[0]
    else:
        return middle_elt(lst[1:-1])


totals = [middle_elt(x) for x in pages_list]
for j,pages in enumerate(pages_list):
    for i,page in enumerate(pages):
        if page in rules:
            for rule in rules[page]:
                if rule in pages[:i]:
                    totals[j] = 0

print(sum(totals))
                    