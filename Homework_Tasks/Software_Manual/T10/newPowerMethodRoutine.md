**Routine Name:** newPowerMethodRoutine

**Author:** Xiang Gao 

**Language:** Python.

**Output:** [Tasksheet_10](https://github.com/GoByMark/math4610/blob/main/Homework_Tasks/Tasksheet_10/Tasksheet%2010.pdf)

Code for newPowerMethodRoutine.py:  
```Python
import numpy as np

def ScaMul(c, arr):
    ScalarProduct = c * arr
    return ScalarProduct

def newPowerMethod(mat, n, vec):
    eigenVector = vec
    for i in range(n):
        eigenVector = np.dot(mat, eigenVector)
        eigenVector = ScaMul((1/np.linalg.norm(eigenVector)), eigenVector)

    eigenValue = np.dot(eigenVector, np.dot(mat, eigenVector)) * (1/np.dot(eigenVector, eigenVector))

    return eigenValue

```
