import numpy as np
import random as rand

def matrixS(n):
    matrix = np.zeros([n, n])
    for i in range(0, n):
        for j in range(0, n):
            matrix[i, j] = rand.randint(1, 11)
    print("The random square matrix of size", n, "is the following\n", matrix)
    return matrix
