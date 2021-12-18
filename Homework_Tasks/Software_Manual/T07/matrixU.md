**Routine Name:** matrixU 

**Author:** Xiang Gao 

**Language:** Python.

**Output:** [Tasksheet_07](https://github.com/GoByMark/math4610/blob/main/Homework_Tasks/Tasksheet_07/Tasksheet%2007.pdf)

Code for matrixU.py:  
```Python
import numpy as np

def matrixU(n, m):
    matrix = np.zeros([n, m])
    for i in range(0, n):
        for j in range(0, m):
            if j < i:
                matrix[i, j] = 0
            else:
                matrix[i, j] = i + j - 1
    print("The upper triangular matrix of size", n, "by", m, "is the following\n", matrix)
    return matrix
```
