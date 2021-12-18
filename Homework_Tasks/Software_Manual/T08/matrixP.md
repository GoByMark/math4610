**Routine Name:** matrixP

**Author:** Xiang Gao 

**Language:** Python.

**Output:** [Tasksheet_08](https://github.com/GoByMark/math4610/blob/main/Homework_Tasks/Tasksheet_08/Tasksheet%2008.pdf)

Code for matrixP.py:  
```Python
import pprint
import scipy
import scipy.linalg   # SciPy Linear Algebra Library

def pivot_matrix(A):
    P, L, U = scipy.linalg.lu(A)
    # pprint.pprint(P)
    return P

```
