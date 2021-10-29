from flask import Flask, request, render_template

import datetime

app = Flask(__name__)

#@app.route("/")
#def index():

@app.get("/")
def home_page():
   return render_template("home.html",
   the_title="welcome!")


@app.route("/hello")
def hello():
    return "hello bababooey"


#@app.get("/home")
#def home_page():
 #  return render_template("home.html",
 #  the_title="welcome!")


@app.get("/showform")
def display_form():
    return render_template("form.html",
    the_title="give us details")

@app.get("/games")
def games():
    return render_template("games.html",
    the_title="My Top 3 Favorite Games Ever")


@app.get("/aboutme")
def aboutme():
    return render_template("aboutme.html",
    the_title="information about this cool dude")


@app.get("/hades")
def hades():
    return render_template("hades.html",
    the_title="Hades")


@app.get("/aceattorney")
def aceattorney():
    return render_template("aceattorney.html",
    the_title="Phoenix Wright Ace Attorney: Trials And Tribulations")


@app.get("/zelda")
def zelda():
    return render_template("zelda.html",
    the_title="The Legend Of Zelda: Majora's Mask")


@app.get("/cv")
def cv():
    return render_template("cv.html",
    the_title="CV")


@app.post("/processform")
def process_form():
    the_name = request.form["thename"]
    the_dob = request.form["thedob"]
    with open("suckers.txt", "a") as sf:
        print(f"{the_name}, {the_dob}", file=sf)
    return f"Hi there, {the_name}, we know you were born on:  {the_dob}."

if __name__=="__main__":
    app.run(debug=True)