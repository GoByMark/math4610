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
To verify if the central difference approximation is actually second order accurate. We can focus on the values associated with h < 10^{-1}.
The error decreases from 0.00034, which suggests that the approximation is actually second order accurate.

### Task 2:
The central difference approximation is actually second order accurate due to the slope generated from the plot. 
From the log-log plot, the approximation begins to fail around the 7-th to 9-th iteration. This is likely due to the limitation of python with decreasing h-value.

![Python Log-Log Graph](https://github.com/GoByMark/math4610/blob/fc8000ef7021a30b30a2c3733014ef5a0f7fed78/Homework_Tasks/Tasksheet_03/pics/YourWay.png)

Since the I only changed two values in the provided code, my own code is the following:

```Python
import matplotlib.pyplot as plt
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

x = []
y = []
for i in range(0, 17):
    x.append(np.log(A[i][0]))
    y.append(np.log(A[i][3]))

fig1 = plt.gcf()
plt.title('Error in the Difference Quotient of the Second Derivative')
plt.xlabel('Increment Values: h')
plt.ylabel('Error in the Approximation')
plt.plot(x, y, label='Log-Log Plot of Error for cos(2.0)')
plt.legend()
plt.show()
fig1.savefig('MyWay.png', bbox_inches='tight')

```

### Task 3:

The routine for single precision is provided below:

```Python
import numpy as py

def sMachineEps():
    one = py.float32(1.0)
    eps = py.float32(1.0)
    for i in range(1, 1000):
        diff = py.float32(one - (one + eps))
        print('{0:<8s}{1:.16f}{2:<12s}{3:.16f}{4:<6s}{5:10f}'.format('Diff =', diff, ' | Eps = ', eps, ' | Counter: ', i))
        if diff == py.float32(0):
            return diff
        eps = py.float32(0.5*eps)
```
With the following code for testing:

```Python
import numpy as py
from dMachineEps import dMachineEps

sMachineEps()
```
And the following output:

![Python Log-Log Graph](https://github.com/GoByMark/math4610/blob/fc8000ef7021a30b30a2c3733014ef5a0f7fed78/Homework_Tasks/Tasksheet_03/pics/single.png)

The routine for double precision is provided below:
```Python
import numpy as py

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
With the following code for testing:

```Python
import numpy as py
from dMachineEps import dMachineEps

dMachineEps()
```
And the following output:

![Python Log-Log Graph](https://github.com/GoByMark/math4610/blob/fc8000ef7021a30b30a2c3733014ef5a0f7fed78/Homework_Tasks/Tasksheet_03/pics/double.png)

### Task 4:
I created the [Software Manual's Table of Contents](https://github.com/GoByMark/math4610/blob/fc8000ef7021a30b30a2c3733014ef5a0f7fed78/Homework_Tasks/Software_Manual/Software_Manual_toc.md). Then I uploaded my precision calculating file. Afterward, I added the links to those files to the Software Manual's Table of Contents.

### Task 5:

### Task 6:
There are difference between static and shared libraries [(https://stackoverflow.com/questions/2649334/difference-between-static-and-shared-libraries)](https://stackoverflow.com/questions/2649334/difference-between-static-and-shared-libraries)
* Shared libraries reduce the amount of code that is duplicated in each program that makes use of the library, keeping the binaries small.
* Static libraries increase the overall size of the binary, but it means that you don't need to carry along a copy of the library that is being used.


There are also different kinds of shared libraries [(https://www.jenkins.io/doc/book/pipeline/shared-libraries/)](https://www.jenkins.io/doc/book/pipeline/shared-libraries/)
* Global Shared Libraries;
* Folder-level Shared Libraries;
* Automatic Shared Libraries
