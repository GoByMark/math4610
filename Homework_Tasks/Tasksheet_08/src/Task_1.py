import numpy as np
import sys

# Reading number of unknowns
n = int(input('Enter number of unknowns: '))

# Making numpy array of n x n+1 size and initializing to zero for storing augmented matrix
A = np.zeros((n, n + 1))

# Making numpy array of n size and initializing to zero for storing solution vector
x = np.zeros(n)

# Reading augmented matrix coefficients
print('Enter Augmented Matrix Coefficients:')
for i in range(n):
    for j in range(n + 1):
        A[i][j] = float(input('a[' + str(i) + '][' + str(j) + ']='))

# Applying Gauss Elimination
for i in range(n):
    if A[i][i] == 0.0:
        sys.exit('Divide by zero detected!')

    for j in range(i + 1, n):
        ratio = A[j][i] / A[i][i]

        for k in range(n + 1):
            A[j][k] = A[j][k] - ratio * A[i][k]

# Back Substitution
x[n - 1] = A[n - 1][n] / A[n - 1][n - 1]

for i in range(n - 2, -1, -1):
    x[i] = A[i][n]

    for j in range(i + 1, n):
        x[i] = x[i] - A[i][j] * x[j]

    x[i] = x[i] / A[i][i]

# Displaying solution
print('\nRequired solution is: ')
for i in range(n):
    print('X%d = %0.2f' % (i, x[i]), end='\t')