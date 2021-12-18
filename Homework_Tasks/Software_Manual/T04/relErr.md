**Routine Name:** sMacEps  

**Author:** Xiang Gao 

**Language:** Python.

**Output:** [Tasksheet_04](https://github.com/GoByMark/math4610/blob/main/Homework_Tasks/Tasksheet_04/Tasksheet%2004.pdf)

Code for sMacEps.cpp:  
```Python
import numpy as np

def relErr(exVal, apprVal):
    relErr = (np.abs(exVal - apprVal))/exVal
    print('The Approximate Value: ', apprVal)
    print('The Exact Value: ', exVal)
    print('The Absolute Error: ', relErr)
```

And the following is the testing code:
```Python
import numpy as np
from relErr import relErr

exVal = input('Enter the Exact Value:\n')

apprVal = input('Enter the Approximate Value:\n')

relErr(np.float32(exVal), np.float32(apprVal))
```
