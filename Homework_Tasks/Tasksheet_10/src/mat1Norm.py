import numpy as np

def mat1Norm(mat):
    tran = np.transpose(mat)
    colSums = []
    for i in range(len(tran)):
        sum = 0
        for j in range(len(tran[i])):
            sum += np.abs(tran[i][j])
        colSums.append(sum)
    return np.max(colSums)