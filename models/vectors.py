import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.feature_extraction.text import TfidfVectorizer

def get_vectors():
  # import data
  df = pd.read_csv('https://raw.githubusercontent.com/mohitgupta-omg/Kaggle-SMS-Spam-Collection-Dataset-/master/spam.csv', encoding = "ISO-8859-1")
  df.rename(columns={
    'v1': 'label',
    'v2': 'message'
  }, inplace=True)
  df.drop(['Unnamed: 2','Unnamed: 3','Unnamed: 4'], 
          axis=1, 
          inplace=True)
  
  # encode labels to numbers
  le = LabelEncoder()
  le.fit(df['label'])
  df['label'] = le.transform(df['label'])

  # split dataset into training and test sets
  X = df['message']
  y = df['label']

  X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

  # encode message to tf-idf vectors
  tfidf = TfidfVectorizer()

  X_train_transformed = tfidf.fit_transform(X_train).toarray()
  X_test_transformed = tfidf.transform(X_test).toarray()

  # scale tf-idf vectors to [0, 1] range
  scaler = StandardScaler()

  X_train_scaled = scaler.fit_transform(X_train_transformed)
  X_test_scaled = scaler.transform(X_test_transformed)
  
  transformers = {
    'tfidf': tfidf,
    'scaler': scaler
  }
  
  return X_train_scaled, X_test_scaled, y_train, y_test, transformers