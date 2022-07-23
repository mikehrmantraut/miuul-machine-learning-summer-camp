##################################################
# Feature Engineering & Data Pre-Processing
#################################################

import numpy as np
import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt
import missingno as msnp
from datetime import date
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.neighbors import LocalOutlierFactor
from sklearn.preprocessing import MinMaxScaler, LabelEncoder, StandardScaler, RobustScaler

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
pd.set_option('display.float_format', lambda x: '%.3f' % x)
pd.set_option('display.width', 500)

def load_application_train():
    data = pd.read_csv("datasets/application_train.csv")
    return data

df = load_application_train()
df.head()

def load():
    data = pd.read_csv("datasets/titanic.csv")
    return data

df = load()
df.head()

## Finding Outliers

# Outliers with Graphical Technique
sns.boxplot(x=df["Age"])
plt.show()

# How to Catch Outliers?
q1 = df["Age"].quantile(0.25)

q3 = df["Age"].quantile(0.75)

iqr = q3 - q1

up = q3 + 1.5 * iqr
low = q1 - 1.5 * iqr

df[(df["Age"] < low) | (df["Age"] > up)]


df[(df["Age"] < low) | (df["Age"] > up)].index

# Is There an Outlier or Not?
df[(df["Age"] < low) | (df["Age"] > up)].any(axis=None)

df[(df["Age"] < low)].any(axis=None)
