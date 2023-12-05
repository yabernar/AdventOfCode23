f = open("Day5/input", 'r')
lst = []
for line in f:
    word = line.rstrip("\n")
    lst.append(word)
f.close()

seeds = list(map(int, lst.pop(0).split()[1:]))
lst.pop(0)
almanac = []

while lst != []:
    if '' in lst: 
        next_block = lst.index('')
        block = lst[1:next_block]
        lst = lst[next_block+1:]
    else:
        block = lst[1:]
        lst = []
    block = [list(map(int, line.split())) for line in block]
    almanac.append(block)

# Part 1
locations = []
for s in seeds:
    current_nbr = s
    for block in almanac:
        for line in block:
            if current_nbr >= line[1] and current_nbr < line[1]+line[2]:
                current_nbr = line[0] + current_nbr - line[1]
                break
    locations.append(current_nbr)

print("The closest location is situated at", min(locations))

# Part 2
def collision_check(range1, range2):
    return range1[0]+range1[1]-1 >= range2[0] and range1[0] < range2[0]+range2[1]-1

def process_range(seed_range, block_nbr):
    if block_nbr >= len(almanac):
        return seed_range[0]
    results = []
    for line in almanac[block_nbr]:
        if collision_check(seed_range, line[1:]):
            start_range = max(line[1], seed_range[0])
            end_range = min(line[1]+line[2]-1, seed_range[0]+seed_range[1]-1)
            results.append(process_range([line[0] + start_range - line[1], end_range - start_range+1], block_nbr+1))
            if seed_range[0] < start_range:
                results.append(process_range([seed_range[0], start_range - seed_range[0]], block_nbr))
            if seed_range[0]+seed_range[1]-1 > end_range:
                results.append(process_range([end_range+1, seed_range[0]+seed_range[1]-end_range-1], block_nbr))
            return min(results)
    return process_range(seed_range, block_nbr+1)

locations = []
seed_ranges = [seeds[i:i+2] for i in range(0,len(seeds),2)]
for s in seed_ranges:
    locations.append(process_range(s, 0))

print("The closest location with the seed ranges is situated at", min(locations))
