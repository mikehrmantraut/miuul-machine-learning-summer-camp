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


# Multiple Linear Regression with OLS Using Scikit-Learn

df = pd.read_csv("datasets/advertising.csv")

X = df.drop('sales', axis=1)
y = df[["sales"]]

# Model

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20, random_state=1)

reg_model = LinearRegression().fit(X_train, y_train)

# bias
reg_model.intercept_

# coefficients (w - weights)
reg_model.coef_

### Prediction

## What is the expected value of the sale based on the following observation values?
# TV: 30
# radio: 10
# newspaper: 40

n = reg_model.intercept_[0] + reg_model.coef_[0][0]*30 + reg_model.coef_[0][1]*10 + reg_model.coef_[0][2]*40

## Review of Prediction Accuracy

# Train RMSE
y_pred = reg_model.predict(X_train)
np.sqrt(mean_squared_error(y_train, y_pred)) # 1.73

# Train R-SQUARE 
reg_model.score(X_train, y_train) # 0.8959

# Test RMSE
y_pred = reg_model.predict(X_test)
np.sqrt(mean_squared_error(y_test, y_pred)) # 1.41

# Test R-SQUARE
reg_model.score(X_test, y_test) # 0.8927

# cv=10 RMSE
np.mean(np.sqrt(-cross_val_score(reg_model,
                                 X,
                                 y,
                                 cv=10,
                                 scoring="neg_mean_squared_error"))) # 1.691


# cv=5 RMSE
np.mean(np.sqrt(-cross_val_score(reg_model,
                                 X,
                                 y,
                                 cv=5,
                                 scoring="neg_mean_squared_error"))) # 1.717
