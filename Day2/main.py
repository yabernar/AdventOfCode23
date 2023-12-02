f = open("Day2/input", 'r')
lst = []
for line in f:
    word = line.rstrip("\n").replace(";"," ;").replace(":","").split()
    lst.append(word)
f.close()

# Part 1

sum_ids = 0
for game in lst:
    possible = True
    for i in range(3, len(game)):
        if "red" in game[i] and int(game[i-1]) > 12: possible = False
        if "green" in game[i] and int(game[i-1]) > 13: possible = False
        if "blue" in game[i] and int(game[i-1]) > 14: possible = False 
    if possible:
        sum_ids += int(game[1])
print("The sum of possible games is", sum_ids)

# Part 2

sum_powers = 0
for game in lst:
    max_blue, max_green, max_red = (0, 0, 0)
    for i in range(3, len(game)):
        if "red" in game[i] and int(game[i-1]) > max_red: max_red = int(game[i-1])
        if "green" in game[i] and int(game[i-1]) > max_green: max_green = int(game[i-1])
        if "blue" in game[i] and int(game[i-1]) > max_blue: max_blue = int(game[i-1])
    sum_powers += max_red * max_blue * max_green
print("The sum of possible games is", sum_powers)