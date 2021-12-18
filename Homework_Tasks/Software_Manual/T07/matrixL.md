**Routine Name:** matrixL

**Author:** Xiang Gao 

**Language:** Python.

**Output:** [Tasksheet_07](https://github.com/GoByMark/math4610/blob/main/Homework_Tasks/Tasksheet_07/Tasksheet%2007.pdf)

Code for matrixL.py:  
```Python
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
    print("The lower triangular matrix of size", n, "by", m, "is the following\n", matrix)
    return matrix
```
