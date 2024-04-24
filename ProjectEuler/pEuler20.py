import math

number = str(math.factorial(100))
res = 0
for digit in number:
    res += int(digit)

print(res)
