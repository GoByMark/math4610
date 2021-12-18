**Routine Name:** matMatPro

**Author:** Xiang Gao 

**Language:** Python.

**Output:** [Tasksheet_09](https://github.com/GoByMark/math4610/blob/main/Homework_Tasks/Tasksheet_09/Tasksheet%2009.pdf)

Code for matMatPro.py:  
```Python
def MatMatPro (mat1, mat2):
    res = [[0 for x in range(len(mat1))] for y in range(len(mat2))]
    for i in range(len(mat1)):
        for j in range(len(mat2[0])):
            for k in range(len(mat2)):
                # resulted matrix
                res[i][j] += mat1[i][k] * mat2[k][j]
    return res
```
