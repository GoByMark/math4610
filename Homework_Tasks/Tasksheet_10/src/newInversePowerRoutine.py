import numpy as np

def ScaMul(c, arr):
    ScalarProduct = c * arr
    return ScalarProduct

def newInvPowerMethod(mat, n, vec):
    eigenVector = vec
    invMat = np.linalg.inv(mat)

    for i in range(n):
        eigenVector = np.dot(invMat, eigenVector)
        eigenVector = ScaMul((1/np.linalg.norm(eigenVector, ord= 2)), eigenVector)

    eigenValue = np.dot(eigenVector, np.dot(mat, eigenVector)) * (1/np.dot(eigenVector, eigenVector))

    return eigenValue