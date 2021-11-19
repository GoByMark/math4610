import numpy as np

def matrixU(n, m):
    matrix = np.zeros([n, m])
    for i in range(0, n):
        for j in range(0, m):
            if j < i:
                matrix[i, j] = 0
            else:
                matrix[i, j] = i + j - 1
    return matrix
