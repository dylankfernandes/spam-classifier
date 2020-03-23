from flask import Flask, request, render_template
import joblib

app = Flask(__name__)

model = joblib.load('models/saved/model.joblib')

@app.route('/')
def main():
  return render_template('index.html')

@app.route('/predict', methods=["POST"])
def classify():
  if request.method == "POST":
    message = request.form['submission']
    classification=list(model.predict([message]))
    return render_template('index.html', classification=classification)

if __name__ == '__main__':
  app.run(debug=True)