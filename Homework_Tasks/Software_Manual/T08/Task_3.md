**Routine Name:** Task_3

**Author:** Xiang Gao 

**Language:** Python.

**Output:** [Tasksheet_08](https://github.com/GoByMark/math4610/blob/main/Homework_Tasks/Tasksheet_08/Tasksheet%2008.pdf)

Code for Task_3.py:  
```Python
import numpy as np
from matrixP import pivot_matrix

np.set_printoptions(precision=2)

def hilmat(n):
    return [[1 / (i + j + 1) for j in range(n)] for i in range(n)]

def inverse(A):
    n = len(A)
    # Create zero matrices for L and U
    L = np.zeros([n, n])
    U = np.zeros([n, n])

    for j in range(n):
        # All diagonal entries of L are set to unity
        L[j][j] = 1.0

        for i in range(j + 1):
            s1 = sum(U[k][j] * L[i][k] for k in range(i))
            U[i][j] = np.matmul(pivot_matrix(A), A)[i][j] - s1

        for i in range(j, n):
            s2 = sum(U[k][j] * L[i][k] for k in range(i))
            L[i][j] = (np.matmul(pivot_matrix(A), A)[i][j] - s2) / U[j][j]

        inverseMat = np.matmul(np.linalg.inv(U), np.linalg.inv(L))
        return inverseMat

for i in range(4, 11):
    x = np.ones(i)
    sol = x * np.linalg.inv(hilmat(i))
    print('n =', i)
    print(sol)

```
