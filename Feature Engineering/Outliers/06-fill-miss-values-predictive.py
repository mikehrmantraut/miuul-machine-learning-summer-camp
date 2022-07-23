#####################################################
# Filling Missing Values with Predictive Values
#####################################################

import numpy as np
import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt
from sklearn.preprocessing import MinMaxScaler

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
pd.set_option('display.float_format', lambda x: '%.3f' % x)
pd.set_option('display.width', 500)

# Data set for large scale application
def load_titanic_application_train():
    data = pd.read_csv("datasets/application_train.csv")
    return data


df_application = load_titanic_application_train()
df_application.head()

# Data set for small scale application
def load():
    data = pd.read_csv("datasets/titanic.csv")
    return data


def grab_col_names(dataframe, cat_th=10, car_th=20):
    
    # cat_cols, cat_but_car
    cat_cols = [col for col in dataframe.columns if dataframe[col].dtypes == 'O']
    num_but_cat = [col for col in dataframe.columns if dataframe[col].nunique() < cat_th and dataframe[col].dtypes != "O"]
    cat_but_car = [col for col in dataframe.columns if dataframe[col].nunique() > car_th and dataframe[col].dtypes == "O"]
    
    cat_cols = cat_cols + num_but_cat
    cat_cols = [col for col in cat_cols if col not in cat_but_car]

    # num_cols
    num_cols = [col for col in dataframe.columns if dataframe[col].dtypes != "O"]
    num_cols = [col for col in num_cols if col not in num_but_cat]

    print(f"Observations: {dataframe.shape[0]}");
    print(f"Variables: {dataframe.shape[1]}");
    print(f"cat_cols: {len(cat_cols)}");
    print(f"num_cols: {len(num_cols)}");
    print(f"cat_but_car: {len(cat_but_car)}");
    print(f"num_but_cat: {len(num_but_cat)}");
    
    return cat_cols, num_cols, cat_but_car


df = load()
df.head()

cat_cols, num_cols, cat_but_car = grab_col_names(df)
num_cols = [col for col in num_cols if col not in "PassengerId"]

dff = pd.get_dummies(df[cat_cols + num_cols], drop_first=True)

scaler = MinMaxScaler()
dff = pd.DataFrame(scaler.fit_transform(dff), columns=dff.columns)
dff.head()


from sklearn.impute import KNNImputer
imputer = KNNImputer(n_neighbors=5)

dff = pd.DataFrame(imputer.fit_transform(dff), columns=dff.columns)
df.head()

dff = pd.DataFrame(scaler.inverse_transform(dff), columns=dff.columns)

df["age_imputed_knn"] = dff[["Age"]]

df.loc[df["Age"].isnull(), ["Age", "age_imputed_knn"]]
df.loc[df["Age"].isnull()]
