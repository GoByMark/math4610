**Routine Name:** newInversePowerRoutine

**Author:** Xiang Gao 

**Language:** Python.

**Output:** [Tasksheet_10](https://github.com/GoByMark/math4610/blob/main/Homework_Tasks/Tasksheet_10/Tasksheet%2010.pdf)

Code for newInversePowerRoutine.py:  
```Python
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

```
