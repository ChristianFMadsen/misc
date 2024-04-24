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


def d(number):
    divisors = findProperDivisors(number)
    res = 0
    for divisor in divisors:
        res += divisor

    return res


total = 0
for n in range(1, 10000):
    x = d(n)
    if x > 0:
        if d(x) == n and x != n:
            total += n


print(total)
