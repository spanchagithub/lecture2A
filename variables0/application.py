from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    x = 12*14
    headline = "enna Ulagame!" + "--- " + str(x)
    return render_template("index.html", headline=headline)

@app.route("/bye")
def bye():
        headline = "Good Bye!"
        return render_template("index.html", headline=headline)
