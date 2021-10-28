from flask import Flask, request

import datetime

app = Flask(__name__)

@app.route("/")
def index():
    return datetime.datetime.now().ctime()


@app.route("/hello")
def hello():
    return "hello bababooey"


@app.get("/home")
def home_page():
    with open("home.html") as f:
        html = f.read()
        return html

        
@app.get("/showform")
def display_form():
    with open("form.html") as f:
        html = f.read()
    return html


@app.post("/processform")
def process_form():
    the_name = request.form["thename"]
    the_dob = request.form["thedob"]
    with open("suckers.txt", "a") as sf:
        print(f"{the_name}, {the_dob}", file=sf)
    return f"Hi there, {the_name}, we know you were born on:  {the_dob}."

if __name__=="__main__":
    app.run(debug=True)