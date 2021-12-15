import numpy as np
from matrixD import matrixD

n = int(input('Enter dimension of the diagonal dominant matrix: '))
mat = matrixD(n)
x = np.zeros(n)

for i in range(n):
    x[i] = i

# Reading tolerable error
tolerable_error = float(input('Enter tolerable error: '))

# Reading maximum number of steps
max_iteration = int(input('Enter maximum number of steps: '))

# Power Method Implementation
lambda_old = 1.0
condition = True
step = 1
while condition:
    x = np.matmul(mat, x)
    # Finding new Eigen value and Eigen vector
    lambda_new = max(abs(x))
    x = x / lambda_new

    # Displaying Eigen value and Eigen Vector
    print('\nSTEP %d' % (step))
    print('----------')
    print('Eigen Value = %0.4f' % (lambda_new))
    # print('Eigen Vector: ')
    # for i in range(n):
        # print('%0.3f\t' % (x[i]))

    # Checking maximum iteration
    step = step + 1
    if step > max_iteration:
        print('Not convergent in given maximum iteration!')
        break

    # Calculating error
    error = abs(lambda_new - lambda_old)
    print('errror=' + str(error))
    lambda_old = lambda_new
    condition = error > tolerable_error