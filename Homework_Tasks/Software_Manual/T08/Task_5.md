**Routine Name:** Task_5

**Author:** Xiang Gao 

**Language:** Python.

**Output:** [Tasksheet_08](https://github.com/GoByMark/math4610/blob/main/Homework_Tasks/Tasksheet_08/Tasksheet%2008.pdf)

Code for Task_5.py:  
```Python
import numpy as np
from Task_4 import GussPivot

np.set_printoptions(precision=2)

def hilmat(n):
    return [[1 / (i + j + 1) for j in range(n)] for i in range(n)]

for i in range(4, 8):
    x = np.ones(i)
    sol = GussPivot(hilmat(i), x)
    print('The solution with n =', i)
    print(sol)

```
