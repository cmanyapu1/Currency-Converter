from flask import Flask, request, render_template, jsonify, session
from converter import Converter


app = Flask(__name__)
app.config["SECRET_KEY"] = "fdfgkjtjkkg45yfdb"


@app.route("/")
def homepage():

    return render_template("homepage.html")

@app.route("/results")
def display_results():
    
    old = request.args["from"]
    new = request.args["to"]
    amount = request.args["amount"]

    currency_converter = Converter(old, new, amount)
    results = currency_converter.convert()

    return render_template("displayresults.html", results=results)
