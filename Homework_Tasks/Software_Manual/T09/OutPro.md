**Routine Name:** OutPro

**Author:** Xiang Gao 

**Language:** Python.

**Output:** [Tasksheet_09](https://github.com/GoByMark/math4610/blob/main/Homework_Tasks/Tasksheet_09/Tasksheet%2009.pdf)

Code for OutPro.py:  
```Python
import numpy as np

def OutPro(arr1, arr2):
    if len(arr1) != len(arr2):
        print('two vectors are not the same length')

    OutPro = np.outer(arr1, arr2)
    return OutPro
```
