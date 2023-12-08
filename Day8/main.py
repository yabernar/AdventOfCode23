from functools import reduce
import math

f = open("Day8/input", 'r')
lst = []
for line in f:
    word = line.rstrip("\n")
    lst.append(word)
f.close()

instructions = lst.pop(0)
lst.pop(0) # Removing blank line
tree = {}
starting_locations = []
for line in lst:
    tree[line[0:3]] = [line[7:10], line[12:15]]
    if line[2] == "A":
        starting_locations.append(line[0:3])

# Part 1
def find_steps_to_end(location):
    step = 0
    while location[2] != "Z":
        if instructions[step%len(instructions)] == "L": location = tree[location][0]
        else: location = tree[location][1]
        step += 1
    return step
print("The number of steps required is", find_steps_to_end("AAA"))

# Part 2
ends = []
for loc in starting_locations:
    ends.append(find_steps_to_end(loc))
gcd = reduce(math.gcd, ends)
ends = [x//gcd for x in ends]
print("The number of steps for all nodes to end with Z is", reduce(lambda x, y: x*y, ends)*gcd)