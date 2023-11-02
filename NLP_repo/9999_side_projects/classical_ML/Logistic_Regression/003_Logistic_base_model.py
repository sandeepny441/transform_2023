import warnings
warnings.filterwarnings("ignore")

import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
# %matplotlib inline

# Create a dataset with the descriptive features and 10 rows
np.random.seed(0)  # for reproducibility
data = {
    'Age': np.random.randint(20, 70, 10),  # Age values between 20 and 70
    'Income': np.random.randint(20000, 100000, 10),  # Income values between 20,000 and 100,000
    'Spending_Score': np.random.rand(10),  # Random float values between 0 and 1
    'Target': ['Yes' if i > 0.5 else 'No' for i in np.random.rand(10)]
}

df = pd.DataFrame(data)

# Create a Target column with 'Low', 'Medium', 'High' based on Spending_Score
bins = [0, 0.33, 0.66, 1]
labels = ['Low', 'Medium', 'High']
df['Target'] = pd.cut(df['Spending_Score'], bins=bins, labels=labels, include_lowest=True)

df['Target'] = df['Target'].map({'Low': 0, 'Medium': 1, 'High': 2})

X = df[['Age', 'Income', 'Spending_Score']]
y = df['Target']


from sklearn.linear_model import LogisticRegression

# Initialize the logistic regression model
clf = LogisticRegression()

# Train the model
clf.fit(X, y)

# Print out the coefficients and intercept
print('Coefficients:', clf.coef_)
print('Intercept:', clf.intercept_)

y_pred = clf.predict(X)

from sklearn.metrics import confusion_matrix

conf_matrix = confusion_matrix(y, y_pred)
conf_matrix

from sklearn.metrics import accuracy_score, f1_score, precision_score, recall_score

# Compute the metrics
accuracy = accuracy_score(y, y_pred)
f1 = f1_score(y, y_pred, average = 'macro')
precision = precision_score(y, y_pred,  average = 'macro')
recall = recall_score(y, y_pred,  average = 'macro')

print("==========Results for base model===============")

# Print the metrics
print(f"Accuracy: {accuracy:.4f}")
print(f"F1 Score: {f1:.4f}")
print(f"Precision: {precision:.4f}")
print(f"Recall: {recall:.4f}")


print("==========Results for optimzed models ==============")

# Define the model
# clf = LogisticRegression()

from sklearn.model_selection import (StratifiedKFold, KFold, 
                                     LeaveOneOut, LeavePOut, 
                                     ShuffleSplit, StratifiedShuffleSplit, GridSearchCV)

# Define cross-validation strategies
cv_strategies = {
    'Stratified K-Fold CV': StratifiedKFold(n_splits=5),
    'K-Fold CV': KFold(n_splits=5),
    'Leave-One-Out CV': LeaveOneOut(),
    'Leave-P-Out CV (P=2)': LeavePOut(p=2),
    'Shuffle Split': ShuffleSplit(n_splits=3, test_size=0.3),
    'Stratified Shuffle Split': StratifiedShuffleSplit(n_splits=5, test_size=0.2)
}

# Define hyperparameters to tune
param_grid = {
    'penalty': ['l1', 'l2', 'elasticnet', 'none'],
    'C': [0.001, 0.01, 0.1, 1, 10, 100],
    'solver': ['newton-cg', 'lbfgs', 'liblinear', 'sag', 'saga'],
    'max_iter': [50, 100, 200],
    'fit_intercept': [True, False],
    'class_weight': [None, 'balanced'],
    'random_state': [0]  # Setting random_state for reproducibility
}


# You can then use each strategy in the GridSearchCV
for strategy_name, strategy in cv_strategies.items():
    grid_clf = GridSearchCV(clf, param_grid, cv=strategy, scoring='accuracy')
    grid_clf.fit(X, y)
    print(f" =========== Results for {strategy_name}:=========== ")
    print(f"Best hyperparameters: {grid_clf.best_params_}")
    print(f"Best accuracy score: {grid_clf.best_score_}\n")



#plot Logistic Regression summary from Statsmodels 

# plot Loglikelihood plots 

