import copy

f = open("Day11/input", 'r')
lst = []
for line in f:
    word = line.rstrip("\n")
    lst.append(list(word))
f.close()

def print_image(universe):
    for line in universe:
        print("".join(line))
    print()

# Part 1
def expand(universe):
    new = []
    for line in universe:
        new.append(line)
        if "#" not in line:
            new.append(line)
    return new

def rotate90degrees(universe):
    return [list(reversed(col)) for col in zip(*universe)]

def rotate_back(universe):
    return rotate90degrees(rotate90degrees(rotate90degrees(universe)))

expanded_universe = copy.deepcopy(lst)
expanded_universe = rotate_back(expand(rotate90degrees(expand(expanded_universe))))

galaxies = []
for i in range(len(expanded_universe)):
    line = expanded_universe[i]
    for j in range(len(line)):
        if line[j] == "#":
            galaxies.append([i, j])

def manhattan_distance(one, two):
    return abs(one[0]-two[0])+abs(one[1]-two[1])

#print_image(expanded_universe)
#print(galaxies)
sum_distances = 0
for s in range(len(galaxies)):
    for d in galaxies[s+1:]:
        sum_distances += manhattan_distance(galaxies[s], d)
print("Sum of all pair distances is", sum_distances)

# Part 2
empty_lines = []
for i in range(len(lst)):
    if "#" not in lst[i]:
        empty_lines.append(i)
empty_columns = []
for j in range(len(lst)):
    if all([line[j] != "#" for line in lst]):
        empty_columns.append(j)

galaxies = []
for i in range(len(lst)):
    line = lst[i]
    for j in range(len(line)):
        if line[j] == "#":
            galaxies.append([i, j])

def bigger_distance(one, two):
    high = [max(one[0], two[0]), max(one[1], two[1])]
    low = [min(one[0], two[0]), min(one[1], two[1])]
    void_crossed = sum([low[0]< l < high[0] for l in empty_lines]) + sum([low[1]< c < high[1] for c in empty_columns])
    return void_crossed * 999999 + manhattan_distance(one, two)

sum_distances = 0
for s in range(len(galaxies)):
    for d in galaxies[s+1:]:
        sum_distances += bigger_distance(galaxies[s], d)
print("Sum of all pair distances is", sum_distances)
