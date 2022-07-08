###########################
# Index Selection
###########################

import numpy as np

a = np.random.randint(10, size=10)
a[0]
a[0:5]
a[0] = 999

m = np.random.randint(10, size=(3, 5))

# (row, column)
m[0, 0]
m[1, 1]
m[2, 3]

m[2, 3] = 999

# numpy array is fixed type data type
# because of that, instead of 2.9 we will get 2
m[2, 3] = 2.9

# all rows and first column (index 0)
m[:, 0]

# second row (index 1) and all columns
m[1, :]

# first two rows and first three columns
m[0:2, 0:3]
