import numpy as np
import pandas as pd
from sklearn import metrics
from sklearn.naive_bayes import GaussianNB
from vectors import get_vectors
import joblib

X_train, X_test, y_train, y_test, _ = get_vectors()

gnb = GaussianNB()

gnb.fit(X_train, y_train)
predictions = gnb.predict(X_test)
accuracy = metrics.accuracy_score(y_test, predictions)

print(f"Naive Bayes Model Accuracy: {(accuracy * 100).round(2)}%")
joblib.dump(gnb, 'saved/nb.joblib')