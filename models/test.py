from vectors import get_vectors
import joblib
import numpy as np
import pandas as pd

_, _, _, _, transformers = get_vectors()
lr_model = joblib.load('models\saved\lr.joblib')

message = "Free entry in 2 a wkly comp to win FA Cup final tkts 21st May 2005. Text FA to 87121 to receive entry question(std txt rate)T&C's apply 08452810075over18's"
vectorized = transformers['tfidf'].transform([message]).toarray()
scaled = transformers['scaler'].transform(vectorized)  

# model_selection = request.form["options"]
# if model_selection == "nb_option":
#   return nb_model.predict(scaled)
# else:
#   return lr_model.predict(scaled)
print(lr_model.predict(scaled))