import numpy as np

def matInfNorm(mat):
    rowSums = []
    for i in range(len(mat)):
        sum = 0
        for j in range(len(mat[i])):
            sum += np.abs(mat[i][j])
        rowSums.append(sum)
    return np.max(rowSums)