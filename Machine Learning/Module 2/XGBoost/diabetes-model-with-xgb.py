#####################################
# Extreme Gradient Boosting (XGBoost)
#####################################
import warnings
import pandas as pd
from sklearn.model_selection import GridSearchCV, cross_validate
from xgboost import XGBClassifier

pd.set_option('display.max_columns', None)
warnings.simplefilter(action='ignore', category=Warning)

df = pd.read_csv("datasets/diabetes.csv")

y = df["Outcome"]
X = df.drop(["Outcome"], axis=1)

# XGBoost
xgboost_model = XGBClassifier(random_state=17)

cv_results = cross_validate(xgboost_model, X, y, cv=5, scoring=["accuracy", "f1", "roc_auc"])
cv_results['test_accuracy'].mean() # 0.7526
cv_results['test_f1'].mean()  # 0.6317
cv_results['test_roc_auc'].mean() # 0.7987

xgboost_params = {"learning_rate": [0.1, 0.01, 0.001],
              "max_depth": [5, 8, 12, 15, None],
              "n_estimators": [100, 500, 1000],
              "colsample_bytree": [None, 0.7, 1]}

xgboost_best_grid = GridSearchCV(xgboost_model, xgboost_params, cv=5, n_jobs=-1, verbose=True).fit(X, y)

xgboost_best_grid.best_params_

xgboost_final = xgboost_model.set_params(**xgboost_best_grid.best_params_, random_state=17).fit(X, y)

cv_results = cross_validate(xgboost_final, X, y, cv=5, scoring=["accuracy", "f1", "roc_auc"])
cv_results['test_accuracy'].mean() # 0.7618
cv_results['test_f1'].mean() # 0.6088
cv_results['test_roc_auc'].mean() # 0.8194
