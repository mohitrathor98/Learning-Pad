# Pandas Series is a one-dimensional labeled array capable of holding data
# of any type (integer, string, float, python objects, etc.).
# The axis labels are collectively called index. Pandas Series is nothing
# but a column in an excel sheet.


# pip install pandas

import pandas as pd
import numpy as np

# Pandas series
lst = [1, 2, 3, 4, 5]
arr = np.array(lst)
print(pd.Series(lst))
# Output:
# 0    1
# 1    2
# 2    3
# 3    4
# 4    5
# dtype: int64


# Pandas Dataframe
# intialise data of lists.
data = {'Name': ['Tom', 'nick', 'krish', 'jack'],
        'Age': [20, 21, 19, 18]}

# Create DataFrame
df = pd.DataFrame(data)

# Print the output.
print(df)
#     Name  Age
# 0    Tom   20
# 1   nick   21
# 2  krish   19
# 3   jack   18


# To Delete a data frame
del df