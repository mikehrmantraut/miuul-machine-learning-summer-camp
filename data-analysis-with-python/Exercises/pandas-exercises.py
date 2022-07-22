import pandas as pd
import seaborn as sns

# 1
df = sns.load_dataset("titanic")
pd.set_option('display.max_columns', None)
pd.set_option('display.width', 500)
df.head()

# 2
df["sex"].value_counts()

# 3
df.nunique()

# 4
df["pclass"].nunique()

# 5
df[["pclass", "parch"]].nunique()

# 6
df["embarked"].dtype
df["embarked"] = df["embarked"].astype("category")

# 7
df[df["embarked"] == "C"]

# 8
df[df["embarked"] != "S"]

# 9
df[(df["age"] < 30) & (df["sex"] == "female")]

# 10
df[(df["fare"] > 500) | (df["age"] > 70)]

# 11
df.isnull().sum()

# 12
df.drop("who", inplace=True, axis=1)

# 13
df["deck"].fillna(df["deck"].mode().iloc[0], inplace=True)

# 14
df["age"].fillna(df["age"].median(), inplace=True)

# 15
df.groupby("survived").agg({"pclass": ["sum", "count", "mean"]}, "")

# 16
def ageFlag():
    age_flag = df["age"].apply(lambda x: 1 if x < 30 else 0)
    df["age_flag"] = age_flag
ageFlag()

# 17
df = sns.load_dataset("Tips")
df.head()

# 18
df.groupby("time").agg({"total_bill":["sum", "min", "max", "mean"]})

# 19
df.groupby(["time", "day"]).agg({"total_bill":["sum", "min", "max", "mean"]})


# 20
df[["total_bill", "tip", "day"]].loc[(df["time"] == "Lunch") & (df["sex"] == "Female")].groupby("day").agg(
    {"total_bill":["sum", "min", "max", "mean"],
    "tip":["sum", "min", "max", "mean"]})


# 21
df.loc[(df["size"] < 3) & (df["total_bill"] > 10)].mean()

# 22
df["total_bill_tip_sum"] = df["total_bill"] + df["tip"]
df["total_bill_tip_sum"]

# 23
female = df["total_bill"].loc[df["sex"] == "Female"].mean()
male = df["total_bill"].loc[df["sex"] == "Male"].mean()

def mission_23(gender, total_bill):
    if (gender == "Female" and total_bill < female) or (gender == "Male" and total_bill < male):
        return 0
    elif (gender == "Female" and total_bill > female) or (gender == "Male" and total_bill > male):
        return 1
df["total_bill_flag"] = df.apply(lambda x: mission_23(x.sex, x.total_bill), axis=1)
df.head()

# 24
print(df.groupby(["sex", "total_bill_flag"]).total_bill_flag.count())

# 25
df.sort_values(by="total_bill_tip_sum", ascending=False)
