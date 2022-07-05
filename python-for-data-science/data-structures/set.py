#######################
# Set
#######################

"""
- Sets are mutable.
- Sets are unordered.
- Set elements are unique. (Duplicate elements are not allowed.)
"""

set1 = set([1, 3, 5])
set2 = set([1, 2, 3])

type(set1)

## difference()
# in set1 but not in set2
set1.difference(set2)

# in set2 but not in set1
set2.difference(set1)

## symmetric_difference()
set1.symmetric_difference(set2)
set2.symmetric_difference(set1)

## intersection()
set1.intersection(set2)

## union() 
set1.union(set2)

## isdisjoint(): Is the intersection of two sets empty?
set1.isdisjoint(set2)
