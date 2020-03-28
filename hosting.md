# HooHacks Demo - Spam Classifier

## 1. Setting Up the Environment

Before you begin, ensure that you have Python 3 (including pip) , a Unix command line, and a text editor installed. I personally recommend using the Anaconda distribution, which comes with most data science packages (including Python) and Visual Studio Code. If you're running Windows, use Git Bash as your Unix command line.

**Installing packages**

For the purpose of this demo, the virtual environment isn't strictly necessary. The purpose of the Unix command line is to run the source command below, so the Unix command line isn't required to work through the workshop.

1. Install the virtual environment package using `pip install virtualenv`.  
2. In the project's root folder, run `virtualenv venv` to create a virtual environment. Having a virtual environment isolates any packages that you install to just that project. 
3. Start the virtual environment by running `source ./venv/Scripts/activate` on the environment. Note that you can deactivate the virtual environment simply by running the `deactivate` command.
4. The libraries that we use in this workshop are listed in the `requirements.txt` file. To install them, simply run `pip install -r requirements.txt`.  In the meantime, take them through the rest of the file system.

## 2. Building A Basic Server

The installation of the libraries in the `requirements.txt` file might take some time to install the requirements. In the meantime, run them through building a basic server.

```python
# server.py
from flask import Flask

app = Flask(__name__)

@app.route('/')
def main():
  return "HooHacks + MLC@UVA Demo"

if __name__ == '__main__':
  app.run(debug=True)
```

We can run the app using `python server.py`.  

## 3. Building Our UI

Now that we've defined our basic server, let's build the UI. Flask uses jinja templates to build user interfaces, which are pretty much HTML, but with built in logic. 

1. Show the `templates/layout.html` file. Show that we're using previously defined styles located in `static/styles.css` and Bootstrap to style our application. Show that `index.html` extends this template.
2. Render the `index.html` template from our server.

```python
# server.py
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def main():
  return render_template('index.html')

if __name__ == '__main__':
  app.run(debug=True)
```

3. Build the user interface

```html
<!--templates/index.html-->
<h1>Spam Classifier</h1>
<p>Enter your message below</p>
<form class="form-group">
  <textarea name="submission" class="form-control" id="submission" row="10"></textarea>
  <button type="submit" class="btn btn-primary">Classify</button>
</form>
```

## 4. Sending Our Message to Our Server

1. Update our HTML to include the method and action attributes to our form.

```html
<!--templates/index.html-->
<h1>Spam Classifier</h1>
<p>Enter your message below</p>
<form class="form-group" action="/predict" method="POST">
  <textarea name="submission" class="form-control" id="submission" row="10"></textarea>
  <button type="submit" class="btn btn-primary">Classify</button>
</form>
```

2. Update our server to include the `/predict` route.

```python
# server.py
from flask import Flask, request, render_template
...
@app.route('/predict', methods=["POST"])
def classify():
  if request.method == "POST":
    message = request.form['submission']
    return render_template('index.html', message=message)
```

3. Update the HTML to show that we got the message.

```html
<h1>Spam Classifier</h1>
<p>Enter your message below</p>
<form class="form-group" action="/predict" method="POST">
  <textarea name="submission" class="form-control" id="submission" row="10"></textarea>
  <button type="submit" class="btn btn-primary">Classify</button>
</form>
{% if message %}
<p>{{ message }}</p>
{% endif %}
```

## 5. Importing and Preprocessing Our Data

1. Rename the columns of the dataframe

```python
# models/save_df.py
df.rename(columns={
  'v1': 'label',
  'v2': 'message'
}, inplace=True)
```

2. Drop unnecessary columns

```python
# models/save_df.py
df.drop(['Unnamed: 2','Unnamed: 3','Unnamed: 4'], 
        axis=1, 
        inplace=True)
```

3. Encode the label column to numeric values

```python
# models/save_df.py
from sklearn.preprocessing import LabelEncoder
...
le = LabelEncoder()
le.fit(df['label'])
df['label'] = le.transform(df['label'])
```

4. Export dataframe to csv file to load later

```python
# models/save_df.py
df.to_csv('models/saved/dataframe.csv')
```

5. To run the file, enter the models directory and run the command `python save_df.py`. This should save a `dataframe.csv` into the `saved` folder.

## 6. Building Our Model

1. Import the preprocessed dataframe

```python
# models/models.py
df = pd.read_csv('models/saved/dataframe.csv', encoding = "ISO-8859-1")
```

2. Separate the dataset into feature set and class.

```python
# models/models.py
X = df['message']
y = df['label']
```

3. Separate the dataset into training and test sets

```python
# models/models.py
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
```

4. Create our classifier.

```python
# models/models.py
clf = Pipeline(steps=[
  ('tfidf', TfidfVectorizer()),
  ('scaler', StandardScaler(with_mean=False)),
  ('lr', LogisticRegression())
])
```

5. Train our model on our training set

```python
# models/models.py
clf.fit(X_train, y_train)
```

6. Make our predictions

```python
# models/models.py
predictions = clf.predict(X_test)
```

7. Determine our accuracy and plot our confusion matrix

```python
# models/models.py
accuracy = metrics.accuracy_score(y_test, predictions)
print(f"Logistic Regression Model Accuracy: {(accuracy * 100).round(2)}%")
```

8. Save our model to our file system.

```python
# models/models.py
joblib.dump(clf, 'models/saved/model.joblib')
```

## 7. Classifying Spam

1. Load our model from our file system

```python
# server.py
model = joblib.load('models/saved/model.joblib')
```

2. Update the post method to classify incoming messages

```python
# server.py
@app.route('/predict', methods=["POST"])
def classify():
  if request.method == "POST":
    message = request.form['submission']
    classification = list(model.predict([message]))
    return render_template('index.html', classification=classification)
```

3. Update the user interface to reflect the classification.

```python
# templates/index.html
<h1>Spam Classifier</h1>
<p>Enter your message below</p>
<form class="form-group" action="/predict" method="POST">
  <textarea name="submission" class="form-control" id="submission" row="10"></textarea>
  <button type="submit" class="btn btn-primary">Classify</button>
</form>
{% if classification %}
{% if classification[0] == 0 %}
<p>Not Spam</p>
{% else %}
<p>Spam</p>
{% endif %}
{% endif %}
```

## 8. Future Steps

1. Use a better model (neural net, SVM, etc.)
2. Use a different metric of accuracy (area under the precision recall curve, etc.)
3. Have fun with it!
