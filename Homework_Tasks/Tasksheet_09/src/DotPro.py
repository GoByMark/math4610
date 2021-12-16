def DotPro(arr1, arr2):
    if len(arr1) != len(arr2):
        print('two vectors are not the same length')
    sum = 0
    for i in range(len(arr1)):
        sum += arr1[i] * arr2[i]
    return sum
