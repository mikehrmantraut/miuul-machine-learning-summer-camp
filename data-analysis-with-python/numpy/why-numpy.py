##################################
# Introduction to NumPy
##################################

# Why use NumPy?
#  NumPy arrays are faster and more compact than Python lists. 
#  An array consumes less memory and is convenient to use. 
#  NumPy uses much less memory to store data 
#  and it provides a mechanism of specifying the data types.
import numpy as np

a = [1, 2, 3, 4]
b = [2, 3, 4, 5]

# Pythonic Way

ab = []

for i in range(0, len(a)):
    ab.append(a[i] * b[i])

# With NumPy
a = np.array([1, 2, 3, 4])
b = np.array([2, 3, 4, 5])
a * b
