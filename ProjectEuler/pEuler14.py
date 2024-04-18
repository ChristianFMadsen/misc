def calcCollatzSequence(number):
    steps = 1
    while number > 1:
        if number % 2 == 0:
            number = number/2
        else:
            number = 3*number+1
        steps += 1

    return steps


maxSteps = [0, 0]
i = 1
while i < 10**6:
    currentSteps = calcCollatzSequence(i)
    if currentSteps > maxSteps[1]:
        maxSteps = [i, currentSteps]
    i += 1

print(f'The starting number under one million that produces the longest chain is {maxSteps[0]} '
      f'with a chain length of {maxSteps[1]}.')
