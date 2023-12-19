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


"""
def convert_textnumbers2(input_string):
    output_string = input_string
#    idx_for_last_number = 0
 #   new_string = ''
    textnumbers = {'one': '1', 'two': '2', 'three': '3', 'four': '4', 'five': '5', 'six': '6', 'seven': '7',
                   'eight': '8', 'nine': '9'}
    for idx, value in enumerate(output_string):
        slice_idx = idx + 1
        substring = output_string[:slice_idx]
        if len(substring) >= 3:
            for textnumber, number in textnumbers.items():
                if textnumber in substring:
                    output_string = substring.replace(textnumber, number) + output_string[slice_idx:]
                    convert_textnumbers2(output_string)

    return output_string




file = open('aoc23_d1p1_data.txt', 'r')


#file = ['two1nine', 'eightwothree', 'abcone2threexyz', 'xtwone3four', '4nineeightseven2', 'zoneight234', '7pqrstsixteen']

sum2 = 0
for string in file:
    cleaned_string = convert_textnumbers2(string)
    print('-----------------------------')
    print(f'{string} ----> {cleaned_string}')
    matches = 0
    first, last = -1, -1
    for idx, value in enumerate(cleaned_string):
        if cleaned_string[idx].isnumeric():
            matches += 1
            last = cleaned_string[idx]
            if matches == 1:
                first = cleaned_string[idx]

    if first == -1 or last == -1:
        print('WOT')
    print(f'Results in: {int(first+last)}')

    sum2 += int(first+last)

print(sum2)
"""