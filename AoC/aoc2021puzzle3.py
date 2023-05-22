#Parsing and functions
dataFile = open("21data/day3.txt", "r")
lines = dataFile.readlines()
dataFile.close()
input = []
for i in lines:
    input.append(i.strip())

#exampleInput = ["00100", "11110", "10110", "10111", "10101", "01111", "00111", "11100", "10000", "11001", "00010", "01010"]
def mostCommonBit(inputList, bitPos):
    counter = 0
    for str in inputList:
        if str[bitPos] == "1":
            counter += 1
        else:
            counter -= 1

    if counter > 0:
        return 1
    elif counter < 0:
        return 0
    else:
        return 2 #if 2 is returned, there is equally as many 1's as 0's in the specified position
def removeEntriesFromList(inputList, bitToRemove, bitPos):
    inputCopy = inputList.copy()
    for str in inputList:
        if str[bitPos] == bitToRemove:
            inputCopy.remove(str)

    return inputCopy
###########################

#Part 1
numberOfBits = len(input[0])
gammaRate = ""
epsilonRate = ""
counter = 0

for i in range(0,numberOfBits):
    if mostCommonBit(input, i) == 1:
        gammaRate += "1"
        epsilonRate += "0"
    elif mostCommonBit(input, i) == 0:
        gammaRate += "0"
        epsilonRate += "1"

print("Power consumption of the submarine:", int(gammaRate, 2)*int(epsilonRate, 2))

#Part 2

oxygenRatingList = input.copy()
currentBitPos = 0
while len(oxygenRatingList)>1:
    bitToKeep = mostCommonBit(oxygenRatingList,currentBitPos)
    if bitToKeep == 1 or bitToKeep == 2:
        oxygenRatingList = removeEntriesFromList(oxygenRatingList, "0", currentBitPos)
    else:
        oxygenRatingList = removeEntriesFromList(oxygenRatingList, "1", currentBitPos)
    currentBitPos += 1


CO2ScrubberList = input.copy()
currentBitPos = 0
while len(CO2ScrubberList)>1:
    bitToRemove = mostCommonBit(CO2ScrubberList, currentBitPos)
    if bitToRemove == 1 or bitToRemove == 2:
        CO2ScrubberList = removeEntriesFromList(CO2ScrubberList, "1", currentBitPos)
    else:
        CO2ScrubberList = removeEntriesFromList(CO2ScrubberList, "0", currentBitPos)
    currentBitPos += 1

print("The life support rating of the submarine is:", int(oxygenRatingList[0],2)*int(CO2ScrubberList[0],2))