from functools import reduce

f = open("Day9/input", 'r')
lst = []
for line in f:
    word = line.rstrip("\n").split()
    word = list(map(int, word))
    lst.append(word)
f.close()

# Part 1 & 2
def extrapolated_values(values, backwards):
    if all(element == 0 for element in values):
        return 0
    new_values = [values[i+1]-values[i] for i in range(len(values)-1)]
    if backwards: return new_values[0] - extrapolated_values(new_values, True)
    else: return new_values[-1] + extrapolated_values(new_values, False)

part1, part2 = 0, 0
for sequence in lst:
    part1 += sequence[-1] + extrapolated_values(sequence, False)
    part2 += sequence[0] - extrapolated_values(sequence, True)
print("The sum of extrapolated values is", part1)
print("The sum of extrapolated history is", part2)