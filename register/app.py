from flask import Flask, render_template, request, redirect


app = Flask(__name__)

# Initialise empty disctionary to save the registrants
REGISTRANTS = {}

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
        
    # save the registrant
    REGISTRANTS[name] = sport

    return redirect("/registrants")

# see regitrants
@app.route("/registrants")
def registrants():
    return render_template("registrants.html", registrants=REGISTRANTS)