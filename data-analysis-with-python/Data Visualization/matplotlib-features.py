##################################
# Matplotlib Features
##################################

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
pd.set_option('display.max_columns', None)
pd.set_option('display.width', 500)

# plot

x = np.array([1, 8])
y = np.array([0, 150])

plt.plot(x, y)
plt.show()

plt.plot(x, y, 'o')
plt.show()

x = np.array([2, 4, 6, 8, 10])
y = np.array([1, 3, 5, 7, 9])

plt.plot(x, y)
plt.show()

plt.plot(x, y, 'o')
plt.show()

# marker
y = np.array([12, 28, 11, 100])

plt.plot(y, marker='o')
plt.show()

plt.plot(y, marker='*')
plt.show()

# markers = ['o', '*', '.', ',' ,'x', 'X', '+', 'P', 's', 'D', 'd', 'p', 'H', 'h']

# line
y = np.array([13, 28, 11, 100])

plt.plot(y, linestyle='dashed')
plt.show()

plt.plot(y, linestyle='dotted')
plt.show()

plt.plot(y, linestyle='dashdot', color='r')
plt.show()

# multiple lines

x = np.array([23, 18, 31, 10])
y = np.array([12, 28, 11, 100])
plt.plot(x)
plt.plot(y)
plt.show()

# labels

x = np.array([80,85,90,95,100,105,110,115,120,125])
y = np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330])
plt.plot(x, y)

# title
plt.title("This is main title")

plt.xlabel("x axis label")

plt.ylabel("y axis label")

plt.grid()
plt.show()

# subplots

# plot 1
x = np.array([80,85,90,95,100,105,110,115,120,125])
y = np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330])
plt.subplot(1, 2, 1)
plt.title("1")
plt.plot(x, y)

# plot 2

x = np.array([8,8,9,9,10,10,10,11,12,12])
y = np.array([24, 25, 26, 27, 28, 29, 30, 31, 32, 33])
plt.subplot(1, 2, 2)
plt.title("2")
plt.plot(x, y)
plt.show()
