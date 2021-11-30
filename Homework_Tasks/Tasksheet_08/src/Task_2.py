import numpy as np
from matrixP import pivot_matrix

A = [[7, 3, -1, 2], [3, 8, 1, -4], [-1, 1, 4, -1], [2, -4, -1, 6]]

n = len(A)

# Create zero matrices for L and U
L = np.zeros([n, n])
U = np.zeros([n, n])

# Perform the LU Decomposition

for j in range(n):
    # All diagonal entries of L are set to unity
    L[j][j] = 1.0

    for i in range(j + 1):
        s1 = sum(U[k][j] * L[i][k] for k in range(i))
        U[i][j] = np.matmul(pivot_matrix(A), A)[i][j] - s1

    for i in range(j, n):
        s2 = sum(U[k][j] * L[i][k] for k in range(i))
        L[i][j] = (np.matmul(pivot_matrix(A), A)[i][j] - s2) / U[j][j]

print("The lower Triangular Matrix is: ")
print(L)
print("The upper Triangular Matrix is: ")
print(U)

