import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder

# import data
df = pd.read_csv('https://raw.githubusercontent.com/mohitgupta-omg/Kaggle-SMS-Spam-Collection-Dataset-/master/spam.csv', encoding = "ISO-8859-1")

# clean dataframe
df.rename(columns={
  'v1': 'label',
  'v2': 'message'
}, inplace=True)

df.drop(['Unnamed: 2','Unnamed: 3','Unnamed: 4'], 
        axis=1, 
        inplace=True)

le = LabelEncoder()
le.fit(df['label'])
df['label'] = le.transform(df['label'])

df.to_csv('saved/dataframe.csv')