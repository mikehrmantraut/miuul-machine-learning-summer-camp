##############################
# Feature Extraction / Regex
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

# Feature Extraction with Regex
df = load()
df.head()

df["NEW_TITLE"] = df.Name.str.extract(' ([A-Za-z]+)\.', expand=False)

df[["NEW_TITLE", "Survived", "Age"]].groupby(["NEW_TITLE"]).agg({"Survived": "mean", "Age": ["count", "mean"]})
