from flask import Flask, render_template, url_for, redirect, request
import pandas as pd
from datetime import datetime

from Predictor import predict

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

#@app.route("/")
#def index(res):
#    return render_template('index.html')

@app.route("/", methods=['POST'])
def handle_data():
    #projectpath = request.form['projectFilepath']
    #if request.method == "POST":
    bud = request.form["bud"]
    pop = request.form["pop"]
    runtime = request.form["runt"]
    date = request.form["rel"]
    dt = datetime.strptime(date, '%Y-%m-%d')

    weekday = dt.weekday() + 1

    data = pd.DataFrame([[bud, pop, runtime, dt.day, weekday, dt.month, dt.year]], columns=["budget", "popularity", "runtime", "release_day", "release_weekday", "release_month", "release_year"])

    print("data:", data)

    result = int(predict(data)[0])

    print ("Prediction:", result)
    
    return render_template("index.html", res = result)

if __name__ == "__main__":
    app.run(debug = True)