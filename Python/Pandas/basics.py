## We have a CSV(not here) with data
## How to read using pandas?
import pandas as pd
df = pd.read_csv('salaries_by_college_major.csv')

## To get the first 5 rows from the sheet
df.head()

# Now that we've got our data loaded into our dataframe, 
# we need to take a closer look at it to help us understand what it is we are working with. 
# This is always the first step with any data science project. Let's see if we can answer the following questions: 

# How many rows does our dataframe have? 
# How many columns does it have?
# What are the labels for the columns? Do the columns have names?
# Are there any missing values in our dataframe? Does our dataframe contain any bad data?

# How to get number of rows and columns of a sheet??
df.shape
# returns (m, n) where m is number of rows and n is number of columns

# What are the columns name in the sheet we are using ??
df.columns

# How to find missing values or junk values in our dataset ??
df.isna()
# this returns a table with the cells with nan values as marked True

# What if we want to check last 5 values of our dataset ??
df.tail()

# How to remove rows with NAN data?
clean_df = df.dropna()

# How to get data of a particular column?? -- Using Square brackets
clean_df['Starting Median Salary']

# and to get max data from that column??
clean_df['Starting Median Salary'].max()

# To get the row index of this maximum value??
row_num = clean_df['Starting Median Salary'].idxmax()

# and to get data at same row but from different column
clean_df['Undergraduate Major'].loc[row_num]
# or
clean_df['Undergraduate Major'][row_num]

clean_df.loc[row_num] # returns all the data at the given row

