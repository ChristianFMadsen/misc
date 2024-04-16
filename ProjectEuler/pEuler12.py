import math


def calcTriangleNumber(number):
    sum = 0
    for i in range(number + 1):
        sum += i

    return sum


def buildTriangleNumberList(amountOfNumbers):
    numberList = []
    i = 1
    while len(numberList) < amountOfNumbers:
        numberList.append(calcTriangleNumber(i))
        i += 1

    return numberList


def findDivisors(number):
    divisors = []
    checkUntil = int(math.sqrt(number))

    for i in range(1, checkUntil + 1):
        if number % i == 0:
            divisors.append(i)
            if i != int(number/i):
                divisors.append(int(number / i))

    return divisors


def minNumberOfDivisors(min):
    i = 1
    while len(findDivisors(calcTriangleNumber(i))) < min:
        i += 1

    triangleNumberWithMinDivisors = calcTriangleNumber(i)
    divisors = findDivisors(triangleNumberWithMinDivisors)
    return [triangleNumberWithMinDivisors, divisors]


answer = minNumberOfDivisors(501)[0]
print(f'The first triangle number to have over 500 divisors is: {answer}')
