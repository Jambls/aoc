grid = []
with open("input.txt") as f:
    for line in f:
        grid.append(line.strip())
        
antennas = {}
antennas_count = 0
for i,line in enumerate(grid):
    for j, elt in enumerate(line):
        if elt != '.':
            if elt in antennas:
                antennas[elt].append([i,j])
            else:
                antennas[elt] = [[i,j]]
            antennas_count += 1

def find_antinodes(locations):
    if len(locations) <= 1:
        return []
    antinodes = []
    for node in locations[1:]:
        y = abs(node[0] - locations[0][0])
        x = abs(node[1] - locations[0][1])
        temp_node_y = node[0]
        temp_node_x = node[1]
        temp_locations_y = locations[0][0]
        temp_locations_x = locations[0][1]
        for i in range(50):
            smaller_y = temp_locations_y - y
            larger_y = temp_node_y + y
            temp_locations_y = smaller_y
            temp_node_y = larger_y
            if node[1] > locations[0][1]:
                smaller_x = temp_locations_x - x
                larger_x = temp_node_x + x
                temp_locations_x = smaller_x
                temp_node_x = larger_x
            else:
                smaller_x = temp_locations_x + x
                larger_x = temp_node_x - x
                temp_locations_x = smaller_x
                temp_node_x = larger_x


            antinodes.append((smaller_y, smaller_x))
            antinodes.append((larger_y, larger_x))
        antinodes.append((node[0], node[1]))
        antinodes.append((locations[0][0], locations[0][1]))

    antinodes = antinodes + find_antinodes(locations[1:])
    return antinodes

antinodes_in_range = []
for key, value in antennas.items():
    antinodes = find_antinodes(value)
    print(antinodes)
    for elt in antinodes:
        if 0 <= elt[0] < len(grid) and 0 <= elt[1] < len(grid[0]):
            antinodes_in_range.append(elt)
print(antinodes_in_range)
print(len(set(antinodes_in_range)))