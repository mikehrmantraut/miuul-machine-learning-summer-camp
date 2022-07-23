#####################################################
# Advanved Techniques
#####################################################

import numpy as np
import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt
from sklearn.preprocessing import MinMaxScaler
import missingno as msno


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

df = load()
df.head()

# examining the structure of missing data
msno.bar(df)
plt.show() 

msno.matrix(df)
plt.show()

msno.heatmap(df)
plt.show()
