dataFile = open("22data/day2.txt", "r")
lines = dataFile.readlines()
dataFile.close()


#A+X = ROCK, B+Y = PAPER, C+Z = SCISSORS
def outcomeOfRound(opponentsPick, yourPick):
    if yourPick == "X": yourPick = "A"
    if yourPick == "Y": yourPick = "B"
    if yourPick == "Z": yourPick = "C"

    if opponentsPick == yourPick:
        return 3

    if opponentsPick == "A":
        if yourPick == "B":
            return 6
        if yourPick == "C":
            return 0

    if opponentsPick == "B":
        if yourPick == "C":
            return 6
        if yourPick == "A":
            return 0

    if opponentsPick == "C":
        if yourPick == "A":
            return 6
        if yourPick == "B":
            return 0

input = []
for i in lines:
    input += [i.strip()]

#input[x][y] - x hand number, y=0 opponents choice, y=2 my choice

scorePt1 = 0
for j in input:
    if j[2] == "X":
        scorePt1 += 1 + outcomeOfRound(j[0], j[2])
    if j[2] == "Y":
        scorePt1 += 2 + outcomeOfRound(j[0], j[2])
    if j[2] == "Z":
        scorePt1 += 3 + outcomeOfRound(j[0], j[2])


print("What would your total score be if everything goes exactly according to your strategy guide?:", scorePt1)

#X = LOSE (0 POINTS), Y = DRAW (3 POINTS), Z = WIN (6 POINTS)
#A ROCK 1, B PAPER 2, C SCISSORS 3

scorePt2 = 0
for k in input:
    if k[2] == "X":
        if k[0] == "A":
            scorePt2 += 3
        if k[0] == "B":
            scorePt2 += 1
        if k[0] == "C":
            scorePt2 += 2

    if k[2] == "Y":
        scorePt2 += 3
        if k[0] == "A":
            scorePt2 += 1
        if k[0] == "B":
            scorePt2 += 2
        if k[0] == "C":
            scorePt2 += 3

    if k[2] == "Z":
        scorePt2 += 6
        if k[0] == "A":
            scorePt2 += 2
        if k[0] == "B":
            scorePt2 += 3
        if k[0] == "C":
            scorePt2 += 1


print("What would your total score be if everything goes exactly according to your strategy guide?:", scorePt2)