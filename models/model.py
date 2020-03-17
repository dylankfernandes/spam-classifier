import numpy as np
import pandas as pd
import joblib
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn import metrics
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression

df = pd.read_csv('saved/dataframe.csv', encoding = "ISO-8859-1")

X = df['message']
y = df['label']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

clf = Pipeline(steps=[
  ('tfidf', TfidfVectorizer()),
  ('scaler', StandardScaler(with_mean=False)),
  ('lr', LogisticRegression())
])

clf.fit(X_train, y_train)
predictions = clf.predict(X_test)
accuracy = metrics.accuracy_score(y_test, predictions)

print(f"Logistic Regression Model Accuracy: {(accuracy * 100).round(2)}%")

sns.heatmap(metrics.confusion_matrix(y_test, predictions), annot=True)
plt.title("Confusion Matrix")
plt.show()

joblib.dump(clf, 'saved/model.joblib')