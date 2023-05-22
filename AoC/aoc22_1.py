dataFile = open("22data/day1.txt", "r")
lines = dataFile.readlines()
dataFile.close()


input = []
for i in lines:
    if i != "\n":
        input += [i.strip()]
    else:
        input += [i]


calorieTotals = []
currentCalories = 0
for j in input:
    if j == "\n":
        calorieTotals += [currentCalories]
        currentCalories = 0
    else:
        currentCalories += int(j)

calorieTotals.sort(reverse=True)

highestCalories = calorieTotals[0]
highestTotalCalories3Elves = calorieTotals[0] + calorieTotals[1] + calorieTotals[2]


print("Find the Elf carrying the most Calories. How many total Calories is that Elf carrying?:", highestCalories)
print("Find the top three Elves carrying the most Calories. How many Calories are those Elves carrying in total?:", highestTotalCalories3Elves)


