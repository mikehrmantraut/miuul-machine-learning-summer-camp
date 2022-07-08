##########################
# Pandas Series
##########################

import pandas as pd

s = pd.Series([10, 77, 12, 4, 5])
type(s)

# index information
s.index

# data type of elements in series
s.dtype

# number of elements 
s.size

# information about dimension
s.ndim

# values of elements in series
s.values
type(s.values)

# first 3 values
s.head(3)

# last 3 values
s.tail(3)
