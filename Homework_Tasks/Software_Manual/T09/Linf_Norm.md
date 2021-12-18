**Routine Name:** Linf_Norm

**Author:** Xiang Gao 

**Language:** Python.

**Output:** [Tasksheet_09](https://github.com/GoByMark/math4610/blob/main/Homework_Tasks/Tasksheet_09/Tasksheet%2009.pdf)

Code for Linf_Norm.py:  
```Python
import numpy as np

def Linf_Norm (arr1):
    norm = np.linalg.norm(arr1, ord=np.inf)
    return norm
```
