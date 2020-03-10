from flask import Flask, request, render_template
import joblib
from models.vectors import get_vectors
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.feature_extraction.text import TfidfVectorizer
from models.dataframe import get_dataframe

app = Flask(__name__)

lr_model = joblib.load('models/saved/lr.joblib')
nb_model = joblib.load('models/saved/nb.joblib')

_, _, _, _, transformers = get_vectors()

@app.route('/')
def main():
  return render_template('index.html')

@app.route('/predict', methods=["POST"])
def classify():
  if request.method == "POST":
    message = request.form["submission"]
    vectorized = transformers['tfidf'].transform([message]).toarray()
    scaled = transformers['scaler'].transform(vectorized)  

    # model_selection = request.form["options"]
    # if model_selection == "nb_option":
    #   return nb_model.predict(scaled)
    # else:
    #   return lr_model.predict(scaled)
    return nb_model.predict(scaled)

if __name__ == '__main__':
  app.run(debug=True)