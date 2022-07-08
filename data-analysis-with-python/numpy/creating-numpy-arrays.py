##########################
# Creating NumPy Arrays
##########################

import numpy as np

np.array([1, 2, 3, 4, 5])
type(np.array([1, 2, 3, 4, 5]))

# array with zeros and data type is integer
np.zeros(10, dtype=int)

# array with ones and data type is float
np.ones(10, dtype=float)

# random 10 integers between 0 and 10 
np.random.randint(0, 10, size=10)

# mean = 10, standard deviation = 4, (3, 4) matrix
np.random.normal(10, 4, (3, 4))

