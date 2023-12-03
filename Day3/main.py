f = open("Day3/input", 'r')
lst = []
for line in f:
    word = line.rstrip("\n")
    lst.append(word)
f.close()

# Part 1 & 2

gears = {}

def check_row(row, start, end, number):
    row = max(0, min(len(lst)-1, row))
    start = max(0, start)
    end = min(len(lst[0])-1, end)
    if '*' in lst[row][start:end]:
        key = str(row)+","+str(start+lst[row][start:end].index("*"))
        if key in gears:
            gears[key].append(number)
        else:
            gears[key] = [number]
    symbols = ''.join(char for char in lst[row][start:end] if char not in ".0123456789")
    return symbols != ""
    
def process_number(row, start, end, number):
    top = check_row(row-1, start-1, end+1, number)
    mid = check_row(row, start-1, end+1, number)
    bot = check_row(row+1, start-1, end+1, number)
    if top or mid or bot: return number
    return 0

sum_parts = 0
for i in range(len(lst)):
    number_start = -1
    for j in range(len(lst[0])):
        if number_start != -1 and lst[i][j] not in "0123456789":
            sum_parts += process_number(i, number_start, j, int(lst[i][number_start:j]))
            number_start = -1
        elif lst[i][j] in "0123456789":
            if number_start == -1:
                number_start = j
    if number_start != -1:
        sum_parts += process_number(i, number_start, len(lst[0]), int(lst[i][number_start:len(lst[0])]))
print("The sum of all engine parts is", sum_parts)

# Part 2
sum_gears = 0
for value in gears.values():
    if len(value) == 2:
        sum_gears += value[0]*value[1]
print("The sum of all the gear ratios is", sum_gears)