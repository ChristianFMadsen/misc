#Part 1
dataFile = open("21data/day1.txt", "r")
lines = dataFile.readlines()
dataFile.close()
puzzleInput = []
for i in lines:
    puzzleInput.append(int(i))



largerThanPreviousCounter = 0
for n in range(1,len(puzzleInput)):
    if puzzleInput[n] > puzzleInput[n-1]:
        largerThanPreviousCounter+=1

print(largerThanPreviousCounter, "measurements are larger than the previous measurement.")


#Part 2
largerThanPreviousSum = 0
for n in range(0, len(puzzleInput)-3):
    sumOne = puzzleInput[n]+puzzleInput[n+1]+puzzleInput[n+2]
    sumTwo = puzzleInput[n+1]+puzzleInput[n+2]+puzzleInput[n+3]
    if sumTwo > sumOne:
        largerThanPreviousSum+=1

print(largerThanPreviousSum, "sums are larger than the previous sum.")