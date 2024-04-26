nameFile = open('22_names.txt', 'r').read()
names = nameFile.split(',')
names = [name.replace('"', '').lower() for name in names]
names.sort()
alphabetPositions = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8, 'i': 9, 'j': 10, 'k': 11, 'l': 12,
                     'm': 13, 'n': 14, 'o': 15, 'p': 16, 'q': 17, 'r': 18, 's': 19, 't': 20, 'u': 21, 'v': 22, 'w': 23,
                     'x': 24, 'y': 25, 'z': 26}

res = 0
for index, name in enumerate(names):
    nameWorth = 0
    for letter in name:
        nameWorth += alphabetPositions[letter]
    res += nameWorth*(index+1)

print(f'What is the total of all the name scores in the file? {res}')
