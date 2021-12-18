**Routine Name:** forSub

**Author:** Xiang Gao 

**Language:** Python.

**Output:** [Tasksheet_08](https://github.com/GoByMark/math4610/blob/main/Homework_Tasks/Tasksheet_08/Tasksheet%2008.pdf)

Code for forSub.py:  
```Python
import numpy as np

def forward_substitution(A, b):
    # Get number of rows
    n = A.shape[0]

    # Allocating space for the solution vector
    y = np.zeros_like(b, dtype=np.double);

    # Here we perform the forward-substitution.
    # Initializing  with the first row.
    y[0] = b[0] / A[0, 0]

    # Looping over rows in reverse (from the bottom  up), starting with the second to last row, because the
    # last row solve was completed in the last step.
    for i in range(1, n):
        y[i] = (b[i] - np.dot(A[i, :i], y[:i])) / A[i, i]
    return y

```
