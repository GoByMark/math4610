**Routine Name:** Task_4

**Author:** Xiang Gao 

**Language:** Python.

**Output:** [Tasksheet_08](https://github.com/GoByMark/math4610/blob/main/Homework_Tasks/Tasksheet_08/Tasksheet%2008.pdf)

Code for Task_4.py:  
```Python
import numpy as np

A = [[7, 3, -1, 2], [3, 8, 1, -4], [-1, 1, 4, -1], [2, -4, -1, 6]]

b = np.ones(4)

def GussPivot(A, b):
    n = len(A)
    M = A
    i = 0
    for x in M:
        x.append(b[i])
        i += 1
    for k in range(n):
        for i in range(k,n):
            if abs(M[i][k]) > abs(M[k][k]):
                M[k], M[i] = M[i],M[k]
            else:
                pass
        for j in range(k + 1, n):
            q = float(M[j][k]) / M[k][k]
            for m in range(k, n+1):
                M[j][m] -= q * M[k][m]
    x = [0 for i in range(n)]
    x[n-1] = float(M[n-1][n]) / M[n-1][n-1]
    for i in range(n-1, -1, -1):
        z = 0
        for j in range(i+1, n):
            z = z + float(M[i][j])*x[j]
        x[i] = float(M[i][n] - z)/M[i][i]
    return x

print(GussPivot(A, b))
```
