import copy


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


correct = [True for _ in pages_list]
for j,pages in enumerate(pages_list):
    for i,page in enumerate(pages):
        if page in rules:
            for rule in rules[page]:
                if rule in pages[:i]:
                    correct[j] = False

pages_incorrect = []
for i,pages in enumerate(pages_list):
    if not correct[i]:
        pages_incorrect.append(pages)


while(True):
    old_pages_incorrect = copy.deepcopy(pages_incorrect)
    for pages in pages_incorrect:
        for i, page in enumerate(pages):
            if page in rules:
                for j, rule in enumerate(rules[page]):
                    if rule in pages[:i]:
                        pages.insert(i+1, rule)
                        pages.remove(rule)
    if pages_incorrect == old_pages_incorrect:
        break


totals = [middle_elt(x) for x in pages_incorrect]
print(sum(totals))
                    