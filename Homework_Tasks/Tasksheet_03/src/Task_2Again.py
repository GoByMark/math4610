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