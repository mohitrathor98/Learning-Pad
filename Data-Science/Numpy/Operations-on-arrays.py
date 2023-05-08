# Arithmetic operations
import numpy as np
arr = np.array([1, 2, 3, 4, 5, 6])
print(arr + 1)
print(arr - 1)
print(arr * 5)
print(arr / 2)
print(arr % 2)
print(arr ** 2)
# Outputs:
# [2 3 4 5 6 7]
# [0 1 2 3 4 5]
# [ 5 10 15 20 25 30]
# [0.5 1.  1.5 2.  2.5 3. ]
# [1 0 1 0 1 0]
# [ 1  4  9 16 25 36]

print(arr.max())
print(arr.min())
# 6
# 1

arr = np.array([[1,2,3],
                [4,5,6],
                [7,8,9]
                ])
print(arr.max(axis = 0)) # get max elements column-wise
print(arr.max(axis = 1)) # get max elements row-wise
print(arr.min(axis = 0)) # get min elements column-wise
print(arr.min(axis = 1)) # get min elements row-wise
print(arr.sum())
#Outputs
# [7 8 9]
# [3 6 9]
# [1 2 3]
# [1 4 7]
# 45

# To perform arithmetic operations on two 
# arrays there shapes must be same
arr2 = np.array([
    [9,8,7],
    [6,5,4],
    [3,2,1]
])

print(arr + arr2)
# [[10 10 10]
#  [10 10 10]
#  [10 10 10]]

print(arr * arr2)
# [[ 9 16 21]
#  [24 25 24]
#  [21 16  9]]

# Dot product of arr x arr2
# Ele(0,0) = (1*9) + (2*6) + (3*3)
print(arr.dot(arr2))
# [[ 30  24  18]
#  [ 84  69  54]
#  [138 114  90]]

# first indexing will work for row
# and seconds indexing for cols
# arr[1 to last row, 0th col]
print(arr[1:, :1])


# Sorting
# Takes three args
# 1. array
# 2. axis: Sorting type ==> 0 : column wise, 1: row wise; if no axis defined then sorts row wise
# 3. kind: Algorithm type
print(np.sort(arr2, axis=1, kind='mergesort'))


# Merging of arrays
arr1 = [[1, 2, 3, 4], [5, 6, 7, 8]]
arr2 = [[8, 7, 6, 5], [4, 3, 2, 1]]

# vertical merging of arrays
np.vstack((arr1, arr2))
# array([[1, 2, 3, 4],
#        [5, 6, 7, 8],
#        [8, 7, 6, 5],
#        [4, 3, 2, 1]])

# horizontal merging of arrays
np.hstack((arr1, arr2))
# array([[1, 2, 3, 4, 8, 7, 6, 5],
#        [5, 6, 7, 8, 4, 3, 2, 1]])