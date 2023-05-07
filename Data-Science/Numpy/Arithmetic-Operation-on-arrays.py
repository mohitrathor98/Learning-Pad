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