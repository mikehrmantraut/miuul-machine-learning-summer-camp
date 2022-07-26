##############################
# Feature Extraction / Binary Features
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

# Binary Features: Flag, Bool, True-False
df = load()

df["NEW_CABIN_BOOL"] = df["Cabin"].notnull().astype('int')

df.groupby("NEW_CABIN_BOOL").agg({"Survived": "mean"})

from statsmodels.stats.proportion import proportions_ztest

test_stat, pvalue = proportions_ztest(count=[df.loc[df["NEW_CABIN_BOOL"] == 1, "Survived"].sum(),
                                             df.loc[df["NEW_CABIN_BOOL"] == 0, "Survived"].sum()],
                                      nobs=[df.loc[df["NEW_CABIN_BOOL"] == 1, "Survived"].shape[0],
                                             df.loc[df["NEW_CABIN_BOOL"] == 0, "Survived"].shape[0]])

print("Test Stat = %.4f, p-value = %.4f" % (test_stat, pvalue))

df.loc[((df['SibSp'] + df['Parch']) > 0), "NEW_IS_ALONE"] = "NO"

df.loc[((df['SibSp'] + df['Parch']) == 0), "NEW_IS_ALONE"] = "YES"

df.groupby("NEW_IS_ALONE").agg({"Survived": "mean"})

test_stat, pvalue = proportions_ztest(count=[df.loc[df["NEW_IS_ALONE"] == 1, "Survived"].sum(),
                                             df.loc[df["NEW_IS_ALONE"] == 0, "Survived"].sum()],
                                      nobs=[df.loc[df["NEW_IS_ALONE"] == 1, "Survived"].shape[0],
                                             df.loc[df["NEW_IS_ALONE"] == 0, "Survived"].shape[0]])
