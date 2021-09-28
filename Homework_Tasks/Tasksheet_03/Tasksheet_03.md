### Task 1:
I used the example from Tasksheet 02, to print out the following table, 
![Python Log-Log Graph](https://github.com/GoByMark/math4610/blob/96b5354084cd307d0c6eebbea41beb097f0aca56/Homework_Tasks/Tasksheet_03/pics/difference.png)
And the following code is used:
```Python
import numpy as np
import math

np.set_printoptions(precision=24)

h = np.zeros(18)
h[0] = 1
h[1] = 0.5

for i in range(2, 18):
    h[i] = math.pow(10, -(i-1))

#print(h)

A = np.zeros([17, 4])
# initialize the Matrix A

for i in range(0, 17):
    x = 2
    A[i][0] = h[i]
    A[i][1] = -np.cos(2)
    A[i][2] = (np.cos(x + h[i]) - 2 * (np.cos(x)) + np.cos(x - h[i])) / (math.pow(h[i], 2))
    A[i][3] = np.abs(A[i][2] - A[i][1])

# print(A)

print("%-28s\t%-28s\t%-28s\t%-28s" % ('h-value', 'Exact', 'Approximation', 'Difference'))

for i in range(0, 17):
    print("%-28.6f\t%-28.6f\t%-28.6f\t%-28.6f" % (A[i][0], A[i][1], A[i][2], A[i][3]))

```
