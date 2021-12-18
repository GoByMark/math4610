**Routine Name:** Linf_Norm_Error

**Author:** Xiang Gao 

**Language:** Python.

**Output:** [Tasksheet_09](https://github.com/GoByMark/math4610/blob/main/Homework_Tasks/Tasksheet_09/Tasksheet%2009.pdf)

Code for Linf_Norm_Error.py:  
```Python
import numpy as np

def Linf_Norm_Error (arr1, arr2):
    norm = np.linalg.norm((arr1 - arr2), ord=np.inf)
    return norm
```
