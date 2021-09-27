import numpy as np

arr = np.array([3, 5 , 'k'])
arr.resize([1,3])
arr2 = np.array([1, 2, 'j'])
arr2.resize([1,3])

arr = np.append(arr, arr2, axis = 0)
print(arr)


arr3 = np.array([9, 7 , 'f'])
arr3.resize([1,3])
arr4 = np.array([13, 26, 'l'])
arr4.resize([1,3])

arr3 = np.append(arr3, arr4, axis = 0)
print(arr3)

#now to append the numpy arrays to a list - one list index for each stock data
data =[]
data.append(arr)
data.append(arr3)
print(data[0][0,1])

