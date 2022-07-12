#######################################
# Selection in Pandas
#######################################

import pandas as pd
import seaborn as sns

df = sns.load_dataset("titanic")
df.head()

df.index
df[0:13]
df.drop(0, axis=0).head() # deletes 0th index (row) and shows it with head()

delete_indexes = [1, 3, 5, 7]
df.drop(delete_indexes, axis=0).head(10)

## to make permanent
# df = df.drop(delete_indexes, axis=0)
# df.drop(delete_indexes, axis=0, inplace=True)

# Convert variable to index
df["age"].head()
df.age.head()

df.index = df["age"]
df.drop("age", axis=1).head()
df.drop("age", axis=1, inplace=True)

# Convert index to variable
df.index

# first way
df["age"] = df.index
df.head()

# second way
df.reset_index().head()
df = df.reset_index().head()
