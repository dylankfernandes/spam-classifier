# HooHacks + MLC@UVA Demo - Spam Classification App
Built with Flask and Scikit-Learn.

## Prerequisites
Make sure that you have the following
* Python 3+ and pip (which comes with Python 3+)
* A Unix command line (for windows users, I personally recommend [Git Bash](https://gitforwindows.org/)). This isn't strictly necessary to complete the workshop, but if you don't want the packages installed globally, this is required.

## Workshop Instructions
If you're going to be participating in the workshop, then download the starter code from the `hoohacks-starter` branch either by running `git clone https://github.com/dylankfernandes/spam-classifier.git -b hoohacks-starter` or downloading the branch as a zip file.

## Running the Completed Demo
To run the demo, you first have to understand what each file does.
* `server.py` - runs the server and loads the user interface.
* `templates/layout.html` - contains the base HTML
* `templates/index.html` - contains the body of the HTML
* `models/saved/` - contains all locally saved models and dataframes for future loading
* `models/save_df.py` - cleans the dataframe and saves the new dataframe to local file structure.
* `models/model.py` - builds and saves the logistic regression model.

To actually run the demo, complete the following steps
1. Install the `virtualenv` package using `pip install virtualenv`.
2. Create a virtual environment using `virtualenv <environment-name>` and start it using `source ./<environment-name>/Scripts/activate`. (Note that the activate script directory might change depending on your operating system. On OS X, you can use `source <environment-name>/bin/activate`)
3. Install the required packages using `pip install -r requirements.txt`. You can manually install them as you come across them if need be, but this will install them all for you. Note that if you add more packages, run `pip freeze > requirements.txt` to save them to your requirements file.
4. Navigate into the `models` directory (`cd models`), create a `saved` directory (`mkdir saved` or manually creating the folder in your file system), and then run `python3 models/save_df.py`. This will save the cleaned dataframe as a csv under the `models/saved` directory.
5. Run `python3 models/model.py`. This will build the model and save it as a `.joblib` file under the `models/saved` directory. At this point, make sure that the `models/saved/` directory contains both the `dataframe.csv` and `model.joblib` files.
6. Go back up to the repo's home directory (`cd ..`) and then run `python3 server.py`.
7. After you are finished using your app, `deactivate` your virtual environment.