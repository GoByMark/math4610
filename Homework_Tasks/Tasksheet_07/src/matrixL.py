import numpy as np
from matrixU import matrixU

def matrixLame(n, m):
    matrix = np.transpose(matrixU(n, m))
    return matrix

def matrixLool(n, m):
    matrix = np.zeros([n, m])
    for i in range(0, n):
        for j in range(0, m):
            if j > i:
                matrix[i, j] = 0
            else:
                matrix[i, j] = i + j - 1
    return matrix