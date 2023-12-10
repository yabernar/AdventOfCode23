import sys
sys.setrecursionlimit(140*140)

f = open("Day10/input", 'r')
lst = []
for line in f:
    word = line.rstrip("\n")
    if "S" in word:
        start = (len(lst), word.index("S"))
    lst.append(word)
f.close()

main_loop = []
for i in range(len(lst)):
    main_loop.append(["."]*len(lst[0]))

# Part 1
def get_pipe(position):
    return lst[position[0]][position[1]]

def add(position, increment):
    return (position[0] + increment[0], position[1] + increment[1])

def dark_soul_mario(position, origin, step):
    main_loop[position[0]][position[1]] = get_pipe(position)
    if position == start: return step
    pipe = get_pipe(position)
    if origin == "South":
        if pipe == "|": return dark_soul_mario(add(position, (-1,0)), "South", step+1)
        if pipe == "F": return dark_soul_mario(add(position, (0,1)), "West", step+1)
        if pipe == "7": return dark_soul_mario(add(position, (0,-1)), "East", step+1)
    if origin == "West":
        if pipe == "-": return dark_soul_mario(add(position, (0,1)), "West", step+1)
        if pipe == "J": return dark_soul_mario(add(position, (-1,0)), "South", step+1)
        if pipe == "7": return dark_soul_mario(add(position, (1,0)), "North", step+1)
    if origin == "North":
        if pipe == "|": return dark_soul_mario(add(position, (1,0)), "North", step+1)
        if pipe == "L": return dark_soul_mario(add(position, (0,1)), "West", step+1)
        if pipe == "J": return dark_soul_mario(add(position, (0,-1)), "East", step+1)
    if origin == "East":
        if pipe == "-": return dark_soul_mario(add(position, (0,-1)), "East", step+1)
        if pipe == "L": return dark_soul_mario(add(position, (-1,0)), "South", step+1)
        if pipe == "F": return dark_soul_mario(add(position, (1,0)), "North", step+1)
    print("Something terribly wrong happened")

#print("Metal yoshi is at ", dark_soul_mario(add(start, (-1,0)), "South", 1)//2)
print("Metal yoshi is at ", dark_soul_mario(add(start, (0,1)), "West", 1)//2)


# Part 2
def print_main_loop():
    for line in main_loop:
        print("".join(line))

def check_parity(string):
    string = string.replace("-","").replace(".","").replace("F7","").replace("FJ","|").replace("L7","|").replace("LJ","")
    return len(string)%2 == 0

in_the_loop = 0
main_loop[start[0]][start[1]] = "L"
for line in main_loop:
    for i in range(len(line)):
        if line[i] == "." and not check_parity("".join(line[i:])):
            line[i] = "X"
            in_the_loop += 1
print("Area of looped surface is", in_the_loop)

print_main_loop()