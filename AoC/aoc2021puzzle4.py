import copy

#Given a board number and a number to mark, replaces the number to mark with an "x" if the number is on the given board
def markNumberOnBoard(listOfBoards, boardToMark, numberToMark):
    for k in range(0, len(listOfBoards[0])): #loops over rows
        for l in range(0, len(listOfBoards[0][0])): #loops over entries in rows
            if listOfBoards[boardToMark][k][l] == numberToMark:
                listOfBoards[boardToMark][k][l] = "x"

    return listOfBoards

#Checks if there's bingo on board with number boardToCheck
def checkForBingo(listOfBoards, boardToCheck):
    # Searches rows for bingo
    for q in range(0, len(listOfBoards[0][0])):
        if listOfBoards[boardToCheck][q].count("x") == 5:
            return 1

    markedInARow = 0
    # Searches columns for bingo
    for w in range(0, len(listOfBoards[0][0])):
        for g in range(0, len(listOfBoards[0])):
            if listOfBoards[boardToCheck][g][w] == "x":
                markedInARow += 1
                if markedInARow == 5:
                    return 1
        markedInARow = 0

    return 0

#Calculates the sum of unmarked numbers on a given board
def sumOfUnmarked(listOfBoards, boardToSum):
    sum = 0
    for p in range(0, len(listOfBoards[0])):
        for u in range(0, len(listOfBoards[0][0])):
            if listOfBoards[boardToSum][p][u] != "x":
                sum += int(listOfBoards[boardToSum][p][u])

    return sum

#Parsing
dataFile = open("21data/day4.txt", "r")
lines = dataFile.readlines()
dataFile.close()
bingoNumbers = [j.rstrip() for j in lines[0].split(',') ] #rstrip removes \n (newline) from the string e.g. "15\n" -> "15"
listOfBoards = []
currentBoard = []

for i in range(2,len(lines)):
    if lines[i] != "\n":
        currentBoard.append(lines[i].split())
    elif lines[i] == "\n":
        listOfBoards.append(currentBoard)
        currentBoard = []

boardsWithoutBingo = copy.deepcopy(listOfBoards) #For use in part 2

#Part 1
bingo = [-1, -1] #[y, z] y is the number of the board on which there is bingo - z is the winning number i.e. the number that triggered the bingo
for n in bingoNumbers:
    for m in range(0,len(listOfBoards)): #loops over boards
        markNumberOnBoard(listOfBoards, m, n)
        if checkForBingo(listOfBoards, m) == 1:
            bingo = [m, n]
            break

    #Breaker if there is bingo on a board
    if bingo != [-1, -1]:
        print("WINNER: [Board number, winning number]", bingo)
        break

print("Final score for the board that wins first:", sumOfUnmarked(listOfBoards, bingo[0])*int(bingo[1]))



#Part 2
boardNumbersWithoutBingo = [i for i in range(99)]
lastBingo = [-1, -1]
for n in bingoNumbers:
    for m in range(0,len(listOfBoards)): #loops over boards
        markNumberOnBoard(listOfBoards, m, n)

    for j in boardNumbersWithoutBingo:
        if checkForBingo(listOfBoards, j) == 1:
            boardNumbersWithoutBingo.remove(j)
        if len(boardNumbersWithoutBingo) == 1:
            lastBingo[0] = j
        if len(boardNumbersWithoutBingo) == 0:
            lastBingo[1] = n
            break

    if lastBingo[1] != -1:
        print("LAST BOARD WITHOUT BINGO: [Board number, winning number]", lastBingo)
        break

print("Final score for the board that wins last :", sumOfUnmarked(listOfBoards, lastBingo[0])*int(lastBingo[1]))