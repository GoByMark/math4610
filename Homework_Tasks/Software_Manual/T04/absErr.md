**Routine Name:** absErr.py  

**Author:** Xiang Gao 

**Language:** Python.

**Output:** [Tasksheet_04](https://github.com/GoByMark/math4610/blob/main/Homework_Tasks/Tasksheet_04/Tasksheet%2004.pdf)

Code for absErr.py:  
```Python
import numpy as np

def absErr(exVal, apprVal):
    absErr = np.abs(exVal - apprVal)
    print('The Approximate Value: ', apprVal)
    print('The Exact Value: ', exVal)
    print('The Absolute Error: ', absErr)
```

And the following is the testing code:
```Python
import numpy as np
from absErr import absErr

exVal = input('Enter the Exact Value:\n')

apprVal = input('Enter the Approximate Value:\n')

absErr(np.float32(exVal), np.float32(apprVal))
```
