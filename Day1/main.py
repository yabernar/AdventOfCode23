f = open("Day1/input", 'r')
lst = []
for line in f:
    word = line.rstrip("\n")
    lst.append(word)
f.close()

# Part 1

numbers = []
for word in lst:
    clean_word = word.strip("abcdefghijklmnopqrstuvwxyz")
    numbers.append(int(clean_word[0])*10+int(clean_word[-1]))
print("Sum of the calibration values :", sum(numbers))

# Part 2
txt = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
replace = ["o1e", "t2o", "t3e", "f4r", "f5e", "s6x", "s7n", "e8t", "n9e"]
numbers = []
for word in lst:
    for digit in range(0, len(txt)):
        word = word.replace(txt[digit], replace[digit])
    clean_word = word.strip("abcdefghijklmnopqrstuvwxyz")
    numbers.append(int(clean_word[0])*10+int(clean_word[-1]))
print("Sum of the corrected calibration values :", sum(numbers))



