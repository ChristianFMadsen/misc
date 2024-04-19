import numpy as np
import math


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
