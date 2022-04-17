from flask import Flask, request, render_template
from flask_cors import cross_origin
import sklearn
import pickle
import pandas as pd


app = Flask(__name__)
model = pickle.load(open("Teaching_assis.pkl", "rb"))


@app.route("/")
@cross_origin()
def home():
    return render_template("index2.html")


@app.route("/predict", methods=["GET", "POST"])
@cross_origin()
def predict():
    if request.method == "POST":


        course_instructor = int(request.form["Course_instructor"])

        native = int(request.form["Native/Not"])

        # Course

        Course= int(request.form["Course"])



        Summer_or_regular_semester= int(request.form["S/R"])

        Class_size = int(request.form['Class_size'])


        prediction = model.predict([[
            native,
            course_instructor,
            Course,
            Summer_or_regular_semester,
            Class_size
        ]])

        output = round(prediction[0],2)

        return render_template('index2.html', prediction_text="Teacher Performance is :- {}".format(output))

    return render_template("index2.html")


if __name__ == "__main__":
    app.run(debug=True)

