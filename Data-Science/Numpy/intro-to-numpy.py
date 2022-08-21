# Google-Colab
## Installing package: !pip install numpy

import numpy as np

# CONVERTING A LIST INTO ARRAY
lst = [1, 2, 3]

arr = np.array(lst)
print(arr)

# FINDING DIMENSION OF THE ARRAY
print(arr.ndim) # prints 1

arr_2d = np.array([[1], [lst]])
print(arr_2d)
print(arr_2d.ndim) # prints 2

# GET SHAPE OF ARRAY
print(arr.shape) # prints (3,)
print(arr_2d.shape) # prints (2, 1)

# GET NUMBER OF ELEMENTS
print(arr.size) # prints 3

# GET DATA TYPE OF ARRAY ELEMENTS
print(arr.dtype)

# GET AN ARRAY FILLED WITH ZEROS
print(np.zeros(shape=(3, 5)))

# GET AN ARRAY FILLED WITH ONES
print(np.ones(shape=(3, 4)))