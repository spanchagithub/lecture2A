import datetime

from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    current = datetime.datetime.now()
    now_is = " Today is " + str(current.year) + "-" + str(current.month) + "-" + str(current.day)
    now = datetime.datetime.now()
    new_year = now.month == 1 and now.day == 1
    return render_template("index.html", now_is=now_is)
    return render_template("index.html", new_year=new_year)
