
def kind(hand):
    cards = hand[0]
    carddict = {}
    for card in cards:
        carddict[card] = carddict[card] +1 if card in carddict else 1
    counts = sorted(list(carddict.values()), reverse = True)
    if counts[0] == 5:
        return 6
    elif counts[0] == 4:
        return 5
    elif counts[0] == 3 and counts[1] == 2:
        return 4
    elif counts[0] == 3:
        return 3
    elif counts[0] == 2 and counts[1] == 2:
        return 2
    elif counts[0] == 2:
        return 1
    else:
        return 0


hands = []
grouped = [[] for i in range(7)]
with open("input.txt", "r") as f:
    for line in f:
        line = line.replace("T", "B").replace("J","C").replace("Q","D").replace("K", "E").replace("A","F")
        hands.append([line[0:5], int(line.strip()[6:])])

for hand in hands:
    grouped[kind(hand)].append(hand)

final = []
for group in grouped:
    group.sort()
    for elt in group:
        final.append(elt)

total = 0
for i,elt in enumerate(final):
    total += (i+1) * elt[1]

print(total)