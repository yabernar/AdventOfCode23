f = open("Day4/input", 'r')
lst = []
for line in f:
    word = line.rstrip("\n").split()
    lst.append(word)
f.close()

# Part 1

score = 0
for card in lst:
    left = list(map(int, card[2:12]))
    right = [int(nbr) for nbr in card[13:]]
    matches = 0
    for nbr in left:
        if nbr in right: matches += 1
    if matches > 0:
        score += 2**(matches-1)
print("The score on the cards is", score)

# Part 2

scratchcards = [1] * len(lst)
for i in range(len(lst)):
    left = list(map(int, lst[i][2:12]))
    right = [int(nbr) for nbr in lst[i][13:]]
    matches = 0
    for nbr in left:
        if nbr in right: matches += 1
    for j in range(matches):
        scratchcards[i+j+1] += scratchcards[i]
print("The final number of cards is", sum(scratchcards))
