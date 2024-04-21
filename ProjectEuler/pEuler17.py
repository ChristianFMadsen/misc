def spellNumber(number):
    def ones(number):
        numSpellings = {
            0: '', 1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six', 7: 'seven', 8: 'eight', 9: 'nine',
            10: 'ten'
        }
        return numSpellings[number]

    def tens(number):
        assert len(str(number)) == 2

        numSpellings = {
            10: 'ten', 11: 'eleven', 12: 'twelve', 13: 'thirteen', 14: 'fourteen', 15: 'fifteen', 16: 'sixteen',
            17: 'seventeen', 18: 'eighteen', 19: 'nineteen'
        }

        if 10 <= number < 20:
            return numSpellings[number]

        tensDigit = int(str(number)[0])
        onesDigit = int(str(number)[1])
        endingSpelling = ones(onesDigit)

        if tensDigit == 2:
            return 'twenty' + endingSpelling
        elif tensDigit == 3:
            return 'thirty' + endingSpelling
        elif tensDigit == 4:
            return 'forty' + endingSpelling
        elif tensDigit == 5:
            return 'fifty' + endingSpelling
        elif tensDigit == 6:
            return 'sixty' + endingSpelling
        elif tensDigit == 7:
            return 'seventy' + endingSpelling
        elif tensDigit == 8:
            return 'eighty' + endingSpelling
        elif tensDigit == 9:
            return 'ninety' + endingSpelling

    def hundreds(number):
        assert len(str(number)) == 3

        hundredsDigit = int(str(number)[0])
        tensDigit = int(str(number)[1])
        onesDigit = int(str(number)[2])

        if tensDigit == 0 and onesDigit == 0:
            return ones(hundredsDigit) + ' hundred'

        if tensDigit == 0:
            endingSpelling = ones(onesDigit)
        else:
            endingSpelling = tens(int(str(number)[-2:]))

        return ones(hundredsDigit) + ' hundred and ' + endingSpelling

    if number < 10:
        return ones(number)
    elif 10 <= number < 100:
        return tens(number)
    elif 100 <= number < 1000:
        return hundreds(number)
    elif number == 1000:
        return 'one thousand'


sum = 0
for i in range(1, 1001):
    spelling = spellNumber(i)
    noSpaces = spelling.replace(' ', '')
    sum += len(noSpaces)

print(sum)
