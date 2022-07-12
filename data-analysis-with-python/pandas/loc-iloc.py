###########################
# loc & iloc
###########################

import pandas as pd
import seaborn as sns

df = sns.load_dataset("titanic")
pd.set_option('display.max_columns', None)
df.head()

# iloc: integer based selection
df.iloc[0:3]
df.iloc[0, 0]

# loc: label based selection
df.loc[0:3]

# df.iloc[0:3, "age"] -> this will give error
df.iloc[0:3, 0:3]
df.loc[0:3, "age"]

col_names = ["age", "embarked", "alive"]
df.loc[0:3, col_names]
