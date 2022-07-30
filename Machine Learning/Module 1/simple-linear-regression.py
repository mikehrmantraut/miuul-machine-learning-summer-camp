#####################################################
# Sales Prediction with Linear Regression
#####################################################

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

pd.set_option('display.float_format', lambda x: '%.2f' % x)

from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, mean_absolute_error
from sklearn.model_selection import train_test_split, cross_val_score


# Simple Linear Regression with OLS Using Scikit-Learn

df = pd.read_csv("datasets/advertising.csv")

X = df[["TV"]]
y = df[["sales"]]


# Model
reg_model = LinearRegression().fit(X, y)

# y_hat = b + w*x

# bias
reg_model.intercept_[0]

# coefficient of TV (w1)
reg_model.coef_[0][0]

## Prediction

# If 150 units of TV are spent, how much sales are expected?

reg_model.intercept_[0] + reg_model.coef_[0][0]*150

# If 500 units of TV are spent, how much sales are expected?
reg_model.intercept_[0] + reg_model.coef_[0][0]*500

# Visualization of Model
g = sns.regplot(x=X, y=y, scatter_kws={'color':'b', 's':9}, ci=False, color='r')
g.set_title(f"Sales = {round(reg_model.intercept_[0], 2)} + TV*{round(reg_model.coef_[0][0], 2)}")
g.set_ylabel("Sale Number")
g.set_xlabel("TV Expenses")
plt.xlim(-10, 310)
plt.ylim(bottom=0)
plt.show()

# Prediction Accuracy

# MSE
y_pred = reg_model.predict(X)
print(mean_squared_error(y, y_pred)) # 10.51
y.mean()
y.std()

# RMSE
np.sqrt(mean_squared_error(y, y_pred)) # 3.24

# MAE
mean_absolute_error(y, y_pred) # 2.54

# R-SQUARE
reg_model.score(X, y)

