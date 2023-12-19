def only_numbers(input_string):
    numbers = []
    textnumbers = {'one': '1', 'two': '2', 'three': '3', 'four': '4', 'five': '5', 'six': '6', 'seven': '7',
                   'eight': '8', 'nine': '9'}
    for idx, value in enumerate(input_string):
        if input_string[idx].isnumeric():
            numbers.append(input_string[idx])
            continue
        for textnumber, number in textnumbers.items():
            if input_string[idx:].startswith(textnumber):
                numbers.append(number)

    return numbers


file = open('aoc23_d1p1_data.txt', 'r')
sum = 0
for string in file:
    number_list = only_numbers(string)
    sum += int(number_list[0]+number_list[-1])

print(sum)
