#####################################
# Cat Boost
#####################################
import warnings
import pandas as pd
from sklearn.model_selection import GridSearchCV, cross_validate
from catboost import CatBoostClassifier

pd.set_option('display.max_columns', None)
warnings.simplefilter(action='ignore', category=Warning)

df = pd.read_csv("datasets/diabetes.csv")

y = df["Outcome"]
X = df.drop(["Outcome"], axis=1)

# CatBoost
catboost_model = CatBoostClassifier(random_state=17, verbose=False)  

cv_results = cross_validate(catboost_model, X, y, cv=5, scoring=["accuracy", "f1", "roc_auc"])
cv_results['test_accuracy'].mean() # 0.7761
cv_results['test_f1'].mean()  # 0.6531
cv_results['test_roc_auc'].mean() # 0.8378

catboost_params = {"learning_rate": [0.1, 0.01],
                   "iterations": [200, 500],
                   "depth": [3, 6]}

catboost_best_grid = GridSearchCV(catboost_model, catboost_params, cv=5, n_jobs=-1, verbose=True).fit(X, y)

catboost_best_grid.best_params_

catboost_final = catboost_model.set_params(**catboost_best_grid.best_params_, random_state=17).fit(X, y)

cv_results = cross_validate(catboost_final, X, y, cv=5, scoring=["accuracy", "f1", "roc_auc"])
cv_results['test_accuracy'].mean() # 0.7708
cv_results['test_f1'].mean() # 0.6309
cv_results['test_roc_auc'].mean() # 0.8420
