####################################
# Operations on Variables
####################################

import pandas as pd
import seaborn as sns
df = sns.load_dataset("titanic")
df.head()

# show all columns
pd.set_option('display.max_columns', None)

"age" in df

df["age"].head()
df.age.head()

df["age"].head()
type(df["age"].head()) # -> pandas.core.series.Series

df[["age"]].head()
type(df[["age"]].head()) # -> pandas.core.frame.DataFrame

df[["age", "alive"]]

col_names = ["age", "adult_male", "alive"]
df[col_names]

df["age2"] = df["age"]**2
df["age3"] = df["age"] / df["age2"]

df.drop("age3", axis=1).head()
df.drop("age3", axis=1, inplace=True)

df.drop(col_names, axis=1).head()

df.loc[:, df.columns.str.contains("age")].head()
df.loc[:, ~df.columns.str.contains("age")].head()
