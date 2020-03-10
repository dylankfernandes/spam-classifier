import numpy as np
import pandas as pd
from sklearn import metrics
from sklearn.linear_model import LogisticRegression
from vectors import get_vectors
import joblib

X_train, X_test, y_train, y_test, _ = get_vectors()

clf = LogisticRegression()

clf.fit(X_train, y_train)
predictions = clf.predict(X_test)
accuracy = metrics.accuracy_score(y_test, predictions)

print(f"Logistic Regression Model Accuracy: {(accuracy * 100).round(2)}%")
joblib.dump(clf, 'saved/lr.joblib')