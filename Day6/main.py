from functools import reduce

f = open("Day6/input", 'r')
lst = []
for line in f:
    word = line.rstrip("\n").split()
    lst.append(word)
f.close()

time = list(map(int, lst[0][1:]))
distances = list(map(int, lst[1][1:]))
# Part 1

winning_ways = []
for race in range(len(time)):
    race_solutions = 0
    for i in range(1, time[race]):
        if (time[race]-i)*i >= distances[race]:
            race_solutions += 1
    winning_ways.append(race_solutions)
print("The product of the number of ways to beat the record is", reduce(lambda x, y: x*y, winning_ways))

# Part 2
t = 56977875
d = 546192711311139
race_solution = 0
for i in range(1, t):
    if (t-i)*i >= d:
        race_solution += 1
print("The number of solutions to the race is", race_solution)