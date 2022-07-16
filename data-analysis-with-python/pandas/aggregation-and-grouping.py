#################################
# Aggregation & Grouping
#################################

import pandas as pd
import seaborn as sns
pd.set_option('display.max_columns', None)
df = sns.load_dataset("titanic")
df.head()

df["age"].mean()

df.groupby("sex")["age"].mean()

df.groupby("sex").agg({"age": "mean"})
df.groupby("sex").agg({"age": ["mean", "sum"]})

df.groupby("sex").agg({"age": ["mean", "sum"],
                        "survived": "mean"})

df.groupby(["sex", "embark_town"]).agg({"age": ["mean", "sum"],
                                        "survived": "mean"})

df.groupby(["sex", "embark_town", "class"]).agg({"age": ["mean", "sum"],
                                        "survived": "mean"})

df.groupby(["sex", "embark_town", "class"]).agg({
    "age": ["mean", "sum"],
    "survived": "mean",
    "sex": "count"})
