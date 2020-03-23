# HooHacks + MLC@UVA Demo - Spam Classification App
Built with Flask and Scikit-Learn.

## Workshop Instructions
If you're going to be participating in the workshop, then download the starter code from the `hoohacks-starter` branch either by running `git clone <this repo> -b hoohacks-starter` command or downloading the branch as a zip file.

## Running the Completed Demo
To run the demo, you first have to understand what each file does.
* `server.py` - runs the server and loads the user interface.
* `templates/layout.html` - contains the base HTML
* `templates/index.html` - contains the body of the HTML
* `models/saved/` - contains all locally saved models and dataframes for future loading
* `models/save_df.py` - cleans the dataframe and saves the new dataframe to local file structure.
* `models/model.py` - builds and saves the logistic regression model.

To actually run the demo, complete the following steps
1. Make sure you have Python 3 installed and a good text editor installed.
2. Install the `virtualenv` package using `pip install virtualenv`.
3. Create a virtual environment using `virtualenv <environment-name>` and start it using `source ./<environment-name>/Scripts/activate`. (Note that the activate script directory might change depending on your operating system. On OS X, you can use `source <environment-name>/bin/activate`)
4. Install the required packages using `pip install -r requirements.txt`. You can manually install them as you come across them if need be, but this will install them all for you. Note that if you add more packages, run `pip freeze > requirements.txt` to save them to your requirements file.
5. Navigate into the `models` directory (`cd models`) and then run `python3 models/save_df.py`. This will save the cleaned dataframe as a csv under the `models/saved` directory.
6. Run `python3 models/model.py`. This will build the model and save it as a `.joblib` file under the `models/saved` directory. 
7. Run `python3 server.py`, after making sure that the `models/saved/` directory contains both the `dataframe.csv` and `model.joblib` files.
8. After you are finished using your app, `deactivate` your virtual environment.