**Routine Name:** Task_5

**Author:** Xiang Gao 

**Language:** Python.

**Output:** [Tasksheet_09](https://github.com/GoByMark/math4610/blob/main/Homework_Tasks/Tasksheet_09/Tasksheet%2009.pdf)

Code for Task_5.py:  
```Python
import numpy as np

ones = [1 for i in range(100)]
solution = np.array(1 for i in range(100))

def jacobi(A, b, tolerance=1e-10, max_iterations=10000):
    x = np.zeros_like(b, dtype=np.double)
    T = A - np.diag(np.diagonal(A))
    for k in range(max_iterations):
        x_old = x.copy()
        x[:] = (b - np.dot(T, x)) / np.diagonal(A)
        error = np.linalg.norm(x - x_old, ord=np.inf) / np.linalg.norm(x, ord=np.inf)
        if error < tolerance:
            break
    return error


def gauss(A, b, tolerance=1e-10, max_iterations=10000):
    x = np.zeros_like(b, dtype=np.double)
    # Iterate
    for k in range(max_iterations):
        x_old = x.copy()
        # Loop over rows
        for i in range(A.shape[0]):
            x[i] = (b[i] - np.dot(A[i, :i], x[:i]) - np.dot(A[i, (i + 1):], x_old[(i + 1):])) / A[i, i]
        # Stop condition
        error = np.linalg.norm(x - x_old, ord=np.inf) / np.linalg.norm(x, ord=np.inf)
        if error < tolerance:
            break
    return error

print('The Error for the Jacobi Iteration is:', jacobi(ones, solution))
print('The Error for the Gaussian Method is:', gauss(ones, solution))
```
