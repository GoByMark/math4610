**Routine Name:** sMacEps  

**Author:** Xiang Gao 

**Language:** C++.

**Output:** [Tasksheet_03](https://github.com/GoByMark/math4610/blob/main/Homework_Tasks/Tasksheet_03/Tasksheet%2003.pdf)

Code for sMacEps.cpp:  
```Python
def dMachineEps():
    one = 1.0
    eps = 1.0
    for i in range(1, 1000):
        diff = one - (one + eps)
        print('{0:<8s}{1:.16f}{2:<12s}{3:.16f}{4:<6s}{5:10f}'.format('Diff =', diff, ' | Eps = ', eps, ' | Counter: ', i))
        if diff == 0:
            return diff
        eps = 0.5*eps
```

And the following is the testing code:
```Python
import numpy as py
from dMachineEps import dMachineEps

dMachineEps()
```
