from flask import Flask, render_template, request, redirect, url_for
from joblib import load

# load the pipeline object
pipeline = load("best_model.joblib")

classes = ['IQ', 'LY', 'QA', 'PL', 'SY', 'TN', 'JO', 'MA', 'SA', 'YE', 'DZ','EG', 'LB', 'KW', 'OM', 'SD', 'AE', 'BH']
def checkDialect(tweet):
    results = pipeline.predict([tweet])[0]
    # get the value counts of different labels predicted
    return classes[results]


# start flask
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html',result='')

@app.route('/', methods=['POST', 'GET'])
def get_data():
    if request.method == 'POST':
        tweet = request.form['search']
        result = checkDialect(tweet)
        return render_template('home.html',result=result)

app.run()
#https://pythonbasics.org/flask-template-data/
