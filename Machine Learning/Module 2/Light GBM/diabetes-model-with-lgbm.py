#####################################
# Light Gradient Boosting Machines (LightGBM)
#####################################
import warnings
import pandas as pd
from sklearn.model_selection import GridSearchCV, cross_validate
from lightgbm import LGBMClassifier

pd.set_option('display.max_columns', None)
warnings.simplefilter(action='ignore', category=Warning)

df = pd.read_csv("datasets/diabetes.csv")

y = df["Outcome"]
X = df.drop(["Outcome"], axis=1)

# LightGBM
lgbm_model = LGBMClassifier(random_state=17)

cv_results = cross_validate(lgbm_model, X, y, cv=5, scoring=["accuracy", "f1", "roc_auc"])
cv_results['test_accuracy'].mean() # 0.7474
cv_results['test_f1'].mean()  # 0.6241
cv_results['test_roc_auc'].mean() # 0.7990

lgbm_params = {"learning_rate": [0.1, 0.01],
              "n_estimators": [100, 300, 500, 1000],
              "colsample_bytree": [0.5, 0.7, 1]}

lgbm_best_grid = GridSearchCV(lgbm_model, lgbm_params, cv=5, n_jobs=-1, verbose=True).fit(X, y)

lgbm_best_grid.best_params_

lgbm_final = lgbm_model.set_params(**lgbm_best_grid.best_params_, random_state=17).fit(X, y)

cv_results = cross_validate(lgbm_final, X, y, cv=5, scoring=["accuracy", "f1", "roc_auc"])
cv_results['test_accuracy'].mean() # 0.7643
cv_results['test_f1'].mean() # 0.6372
cv_results['test_roc_auc'].mean() # 0.8147

