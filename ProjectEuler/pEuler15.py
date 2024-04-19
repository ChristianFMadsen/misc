import random
import numpy as np
import math


def randomAttempt():
    def generateRandomPath(length):
        directions = ['d', 'r']
        path = ''

        while len(path) < length:
            if path.count('d') == length / 2:
                while len(path) < length:
                    path = path + 'r'
                    break

            elif path.count('r') == length / 2:
                while len(path) < length:
                    path = path + 'd'
                    break

            else:
                rand = random.randint(0, 1)
                currentDirection = directions[rand]
                path = path + currentDirection

        return path

    def invertPath(path):
        invertedPath = ''
        for i in path:
            if i == 'd':
                invertedPath = invertedPath + 'r'
            else:
                invertedPath = invertedPath + 'd'

        return invertedPath

    uniquePaths = []
    consecDups = 0
    while consecDups < 50:
        path = generateRandomPath(20)
        invPath = invertPath(path)
        if path not in uniquePaths:
            uniquePaths.append(path)
            consecDups = 0

        if invPath not in uniquePaths:
            uniquePaths.append(invPath)
            consecDups = 0

        if path in uniquePaths or invPath in uniquePaths:
            consecDups += 1


# Number of paths follows Pascal's triangle
# This boils down to a combinatorics problem equivalent to n choose k; for a n-by-n grid we must do n steps to the right
# and n steps down to reach the corner i.e. from 2n steps we choose n
print(math.comb(40, 20))

# Alternatively calculate how many paths that lead into each grid point all the way to the end point
# For a i-by-j grid set rows = i+1 and cols = j+1.
# (The extra row and column is needed to count paths that uses the grid edges [e.g. first example on problem page])
rows = 21
cols = 21
pathMatrix = np.zeros((rows, cols))
pathMatrix[0][0] = 1
for r in range(rows):
    for c in range(cols):
        if r > 0:
            pathMatrix[r][c] += pathMatrix[r-1][c]
        if c > 0:
            pathMatrix[r][c] += pathMatrix[r][c-1]

print(pathMatrix[rows-1][cols-1])
