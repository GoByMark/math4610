**Routine Name:** matrixS 

**Author:** Xiang Gao 

**Language:** Python.

**Output:** [Tasksheet_07](https://github.com/GoByMark/math4610/blob/main/Homework_Tasks/Tasksheet_07/Tasksheet%2007.pdf)

Code for matrixS.py:  
```Python
import numpy as np
import random as rand

def matrixS(n):
    matrix = np.zeros([n, n])
    for i in range(0, n):
        for j in range(0, n):
            matrix[i, j] = rand.randint(1, 11)
    print("The random square matrix of size", n, "is the following\n", matrix)
    return matrix

```
