from flask import Flask, render_template, request


app = Flask(__name__)

SPORTS = ['Football', 'Netball', 'Pool']

# default route
@app.route("/")
def index():
    return render_template("index.html", sports=SPORTS)

# register route
@app.route("/register", methods=["GET", "POST"])
def register():
    name = request.form.get("name")
    # sports = request.form.getall("sport")

    if not name:
        return render_template("failure.html")
    for sport in request.form.getlist("sport"):
        if sport not in SPORTS:
            return render_template("failure.html")
    return render_template("success.html")