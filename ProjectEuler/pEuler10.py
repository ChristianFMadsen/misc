#Problem 10
import math
import numpy as np
import time

listOfPrimes = np.zeros(200000)
listOfPrimes[0]=2; listOfPrimes[1]=3; listOfPrimes[2]=5; listOfPrimes[3]=7;
listIndex = 4;


tic = time.perf_counter()
for i in range(4,1000000):
    candidate = 2*i+1
    for j in range(0,len(listOfPrimes)):
        if candidate/listOfPrimes[j]%1 == 0:
            break
        if listOfPrimes[j]==0 or listOfPrimes[j]>math.sqrt(candidate):
            listOfPrimes[listIndex] = candidate
            listIndex = listIndex + 1
            break

toc = time.perf_counter()
print(toc-tic)

listOfPrimes = listOfPrimes[listOfPrimes != 0]
print(sum(listOfPrimes))

