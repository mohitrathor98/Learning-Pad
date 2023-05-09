# Import pandas
import pandas as pd

df = pd.read_csv('example1.csv')

# Get data for a specific col
print(df['Magnitude'])
# 0        6.0
# 1        5.8
# 2        6.2
# 3        5.8
# 4        5.8
#         ... 
# 23407    5.6
# 23408    5.5
# 23409    5.9
# 23410    6.3
# 23411    5.5
# Name: Magnitude, Length: 23412, dtype: float64

# Get data for multiple cols
print(df[['Magnitude', 'Latitude']])
#        Magnitude  Latitude
# 0            6.0   19.2460
# 1            5.8    1.8630
# 2            6.2  -20.5790
# 3            5.8  -59.0760
# 4            5.8   11.9380
# ...          ...       ...
# 23407        5.6   38.3917
# 23408        5.5   38.3777
# 23409        5.9   36.9179
# 23410        6.3   -9.0283
# 23411        5.5   37.3973

# [23412 rows x 2 columns]

# Get column labels of the data frame
print(df.columns)
# Index(['Date', 'Latitude', 'Longitude', 'Magnitude'], dtype='object')
