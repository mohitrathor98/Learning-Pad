import numpy as np

# GENERATE RANDOM NUMBERS
np.random.random((3,3)) # random numbers: generated from 0 to 1
# array([[0.72879603, 0.62758484, 0.73677306],
#       [0.52201975, 0.34863556, 0.59871419],
#       [0.27719029, 0.96160005, 0.54444138]])

np.random.random() # generates a single random
# 0.059646501243579064


# RANGE AND LINSPACE
np.arange(1, 10, 2) # from start to end-1, step:2
# array([1, 3, 5, 7, 9])


np.linspace(1, 10, 5) # from start to end and gives m(5) values equidistant from one another
# array([ 1.  ,  3.25,  5.5 ,  7.75, 10.  ])

np.linspace(1, 10, 10)
# array([ 1.,  2.,  3.,  4.,  5.,  6.,  7.,  8.,  9., 10.])


# RESHAPING ARRAY
arr = np.random.random((3, 1))

arr = np.reshape(arr, (1, 3))
# intial size of elements (number of elements in the list) should
# be equal to final size of elements (3, 4) can be converted to (6, 2) but not to (2, 2)

# FLATTENING ARRAY
arr.flatten() # converts array to 1D