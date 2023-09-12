## Goals
# Extend our regression model routines to support multiple features
# Extend data structures to support multiple features
# Rewrite prediction, cost and gradient routines to support multiple features
# Utilize NumPy np.dot to vectorize their implementations for speed and simplicity

import copy, math
import numpy as np
import matplotlib.pyplot as plt
plt.style.use('./deeplearning.mplstyle')
np.set_printoptions(precision=2)  # reduced display precision on numpy arrays

### PROBLEM STATEMENT

# You will use the motivating example of housing price prediction. '
# The training dataset contains three examples with four features (size, bedrooms, floors and, age) shown in the table below. 
# 
# Note that, unlike the earlier labs, size is in sqft rather than 1000 sqft. This causes an issue, which you will solve in the next lab!

# Size (sqft)	Number of Bedrooms	Number of floors	Age of Home	Price (1000s dollars)
# 2104	5	1	45	460
# 1416	3	2	40	232
# 852	2	1	35	178
# You will build a linear regression model using these values so you can then predict the price for other houses. 
# 
# For example, a house with 1200 sqft, 3 bedrooms, 1 floor, 40 years old.

X_train = np.array([[2104, 5, 1, 45], [1416, 3, 2, 40], [852, 2, 1, 35]])
y_train = np.array([460, 232, 178])


# data is stored in numpy array/matrix
print(f"X Shape: {X_train.shape}, X Type:{type(X_train)})")
print(X_train)
print(f"y Shape: {y_train.shape}, y Type:{type(y_train)})")
print(y_train)

## OUTPUT::
# X Shape: (3, 4), X Type:<class 'numpy.ndarray'>)
# [[2104    5    1   45]
#  [1416    3    2   40]
#  [ 852    2    1   35]]
# y Shape: (3,), y Type:<class 'numpy.ndarray'>)
# [460 232 178]


## Parameter Vector w, b

# 𝐰 is a vector with  𝑛 elements.
# Each element contains the parameter associated with one feature.
# in our dataset, n is 4.

# 𝑏 is a scalar parameter.

# For demonstration,  𝐰 and 𝑏 will be loaded with some initial selected values that are near the optimal.  
# 𝐰 is a 1-D NumPy vector.

b_init = 785.1811367994083
w_init = np.array([ 0.39133535, 18.75376741, -53.36032453, -26.42131618]) # ==> Initial selected values that are near optimal
print(f"w_init shape: {w_init.shape}, b_init type: {type(b_init)}")

# w_init shape: (4,), b_init type: <class 'float'>