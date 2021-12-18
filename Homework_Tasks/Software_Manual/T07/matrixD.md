**Routine Name:** matrixD 

**Author:** Xiang Gao 

**Language:** Python.

**Output:** [Tasksheet_07](https://github.com/GoByMark/math4610/blob/main/Homework_Tasks/Tasksheet_07/Tasksheet%2007.pdf)

Code for matrixD.py:  
```Python
import numpy as np
import random as rand

def matrixD(n):
    matrix = np.zeros([n, n])
    a = rand.randint(1, 27)
    for i in range(0, n):
        for j in range(0, n):
            if j != i:
                matrix[i, j] = 0
            else:
                matrix[i, j] = a
    print("The random diagonal matrix of size", n, "is the following\n", matrix)
    return matrix
```
