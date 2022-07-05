#####################
# Tuple
#####################

"""
Tuples are immutable.
Typles are ordered.
"""

t = ("john", "mark", 1, 2)
type(t)

t[0]
t[0:3]

# t[0] = 99 -> this will raise TypeError.

t = list(t)
t[0] = 99
t = tuple(t)
