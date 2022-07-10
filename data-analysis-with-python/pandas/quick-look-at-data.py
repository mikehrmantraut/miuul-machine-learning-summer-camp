#######################
# Quick Look at Data
#######################

import pandas as pd
import seaborn as sns

df = sns.load_dataset("titanic")
df.head()
df.tail()
df.shape # row number, column number
df.info
df.columns
df.index 
df.describe().T # count-mean-std-min
df.isnull()
df.isnull().values
df.isnull().values.any()
df.isnull().sum() # how many missing values
df["sex"].value_counts()
