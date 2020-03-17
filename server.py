from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def main():
  return render_template('index.html')

@app.route('/predict', methods=["POST"])
def classify():
  if request.method == "POST":
    message = request.form['submission']
    return render_template('index.html', message=message)

if __name__ == '__main__':
  app.run(debug=True)