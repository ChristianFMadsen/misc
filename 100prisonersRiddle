# 100 prisoners riddle - Veritasium
import numpy as np


def prisonerRiddleSimulation():
    boxNumbers = np.arange(100)  # Numbers for the boxes containing the shuffled prisonerIDs
    prisonerIDs = np.arange(100)  # Numbers for prisoner IDs
    np.random.shuffle(prisonerIDs)  # Shuffle the prisoner ID numbers

    # Create matrix containing box numbers in first column and shuffled prisoner IDs in second column i.e. the first
    # column in the matrix contains the box number and the second column contains the prisoner ID that is inside that
    # box.
    number_ID_matrix = np.array([boxNumbers, prisonerIDs]).transpose()
    # print(number_ID_matrix)

    # Variable to control whether to stop the search for the prisoners ID. If the length of the loop is greater than 50
    # then all the prisoners die so we can stop checking through the rest of the prisoners loops.
    terminateSearch = False
    for prisonerIndex in range(100):  # Index of the prisoner who is searching his loop
        firstEntry = number_ID_matrix[prisonerIndex][1]  # Prisoner goes to the box with his number on it
        latestEntry = number_ID_matrix[firstEntry][
            1]  # Now goes to the box with the number that was inside the first opened box
        lengthOfLoop = 1  # Sets the length of the current loop to 1
        while latestEntry != firstEntry:  # Search until we get back to the original box
            latestEntry = number_ID_matrix[latestEntry][1]  # The number found inside the most recent box checked
            lengthOfLoop = lengthOfLoop + 1  # Increase length of the loop
            if lengthOfLoop > 50:  # Stops the search if the length is greater than 50 - the prisoners lost in this case
                terminateSearch = True
                # print("You lost")
                break

        # print(lengthOfLoop)
        if terminateSearch:  # Terminates searching since the game is lost if terminateSearch = True
            break

    return terminateSearch  # Returns True for a lost game and False for a won game


numberOfSimulations = 10 ** 5  # Sets the number of times to run the simulation
numberOfLostGames = 0  # Records amount of lost games
for j in range(numberOfSimulations):  # Loop that runs the simulations
    if prisonerRiddleSimulation():
        numberOfLostGames = numberOfLostGames + 1

failRate = numberOfLostGames / numberOfSimulations  # Calculate fail rate
successRate = 1 - failRate  # Calculate success rate
print(successRate)
