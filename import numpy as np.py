import numpy as np

arr = []
arr2 = []
arr3 =[]
arr4 = []

arr = [3,4,5]
arr2 = [1, 2, 3]
arr3 = ['a', 'b', 'c']
arr4 = ['d', 'e', 'f']

np.append(arr, arr2)
arr3.append( arr4)
print(arr)
print(arr3)
arr.append(arr3)
print(arr)