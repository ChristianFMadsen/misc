file = open('aoc23_d1p1_data.txt', 'r')
sum = 0
for string in file:
    matches = 0
    first, last = -1, -1
    for idx, value in enumerate(string):
        if string[idx].isnumeric():
            matches += 1
            last = string[idx]
            if matches == 1:
                first = string[idx]

    sum += int(first+last)

print(sum)