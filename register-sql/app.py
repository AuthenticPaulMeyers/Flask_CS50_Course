from flask import Flask, render_template, request, redirect
from cs50 import SQL

app = Flask(__name__)

# create a dabatase connection
db = SQL("sqlite:///froshims.db")

SPORTS = ['Football', 'Netball', 'Pool']

# default route
@app.route("/")
def index():
    return render_template("index.html", sports=SPORTS)

# register route
@app.route("/register", methods=["GET", "POST"])
def register():
    name = request.form.get("name")
    sport = request.form.get("sport")

    # validate name
    if not name:
        return render_template("error.html", message="Missing name")
    
    # validate sport
    if not sport:
        return render_template("error.html", message="Missing sport")
    if sport not in SPORTS:
        return render_template("error.html", message="Invalid sport")
    return render_template("success.html")
    # save the registrant into the database
    db.execute("INSERT INTO registrants (name, sport) VALUES (?, ?)", name, sport)

    return redirect("/registrants")

# see regitrants
@app.route("/registrants")
def registrants():
    registrants = db.execute("SELECT id, name, sport FROM registrants order by name")
    return render_template("registrants.html", registrants=registrants)