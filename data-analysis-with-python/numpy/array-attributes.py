##################################
# Attributes of NumPy Arrays
##################################

import numpy as np

# ndim -> dimension number
# shape -> shape of an array
# size -> total number of elements
# dtype -> data type of an array

a = np.random.randint(10, size=5)
a.ndim    # -> 1
a.shape   # -> (5, )
a.size    # -> 5
a.dtype   # -> 'int64'
