#######################################
# KNN
#######################################

import pandas as pd
from sklearn.metrics import classification_report, roc_auc_score
from sklearn.model_selection import GridSearchCV, cross_validate
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import StandardScaler
pd.set_option('display.max_columns', None)

# Exploratory Data Analysis

df = pd.read_csv("datasets/diabetes.csv")

df.head()
df.shape
df.describe().T
df["Outcome"].value_counts()

# Data Pre-Processing & Feature Engineering

y = df["Outcome"]
X = df.drop(["Outcome"], axis=1)

X_scaled = StandardScaler().fit_transform(X)

X = pd.DataFrame(X_scaled, columns=X.columns)

# Modeling & Prediction

knn_model = KNeighborsClassifier().fit(X, y)

random_user = X.sample(1, random_state=45)

knn_model.predict(random_user)

##  Model Evaluation

# y_pred for Confusion Matrix
y_pred = knn_model.predict(X)

# y_prob for AUC
y_prob = knn_model.predict_proba(X)[:, 1]

print(classification_report(y, y_pred))

# Accuracy -> 0.83
# F1-Score -> 0.74

# AUC
roc_auc_score(y, y_prob) # 0.9017

cv_results = cross_validate(knn_model, X, y, cv=5, scoring=["accuracy", "f1", "roc_auc"])

cv_results['test_accuracy'].mean() # 0.73
cv_results['test_f1'].mean()       # 0.59
cv_results['test_roc_auc'].mean()  # 0.78

## Hyperparameter Optimization

knn_model = KNeighborsClassifier()
knn_model.get_params()

knn_params = {"n_neighbors": range(2, 50)}

knn_gs_best = GridSearchCV(knn_model, knn_params, cv=5, n_jobs=-1, verbose=1).fit(X, y)
knn_gs_best.best_params_

## Final Model

knn_final = knn_model.set_params(**knn_gs_best.best_params_).fit(X, y)

cv_results = cross_validate(knn_model, X, y, cv=5, scoring=["accuracy", "f1", "roc_auc"])

cv_results['test_accuracy'].mean() # 0.76, before 0.73
cv_results['test_f1'].mean()       # 0.61, before 0.59
cv_results['test_roc_auc'].mean()  # 0.81, before 0.78

