def findProperDivisors(number):
    divisors = []
    checkUntil = int(number**0.5)

    for i in range(1, checkUntil + 1):
        if number % i == 0:
            divisors.append(i)
            if i != int(number/i):
                divisors.append(int(number / i))

    divisors.remove(number)
    divisors.sort()
    return divisors


upperBound = 28123
abundantNumbers = []

for i in range(1, upperBound+1):
    divisors = findProperDivisors(i)
    if sum(divisors) > i:
        abundantNumbers.append(i)


totalAbundantNumbers = len(abundantNumbers)
numbers = set(x for x in range(upperBound))

for i in range(totalAbundantNumbers):
    j = i
    while j < totalAbundantNumbers:
        sumAbundantNumbers = abundantNumbers[i] + abundantNumbers[j]
        if sumAbundantNumbers > 28123:
            break
        elif sumAbundantNumbers in numbers:
            numbers.discard(sumAbundantNumbers)
        j += 1

print(f'Sum of all positive integers which cannot be written as the sum of two abundant numbers: {sum(numbers)}')
