##############################
# Feature Extraction / Text
##############################
import pandas as pd

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
pd.set_option('display.float_format', lambda x: '%.3f' % x)
pd.set_option('display.width', 500)

# Data set for small scale application
def load():
    data = pd.read_csv("datasets/titanic.csv")
    return data

# Feature Extraction from Text
df = load()
df.head()

# Letter Count
df["NEW_NAME_COUNT"] = df["Name"].str.len()

# Word Count
df["NEW_NAME_WORD_COUNT"] = df["Name"].apply(lambda x: len(str(x).split(" ")))

df["NEW_NAME_DR"] = df["Name"].apply(lambda x: len([x for x in x.split() if x.startswith("Dr")]))

df.groupby("NEW_NAME_DR").agg({"Survived": ["mean", "count"]})
