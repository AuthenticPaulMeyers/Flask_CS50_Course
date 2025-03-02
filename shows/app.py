from flask import Flask, render_template, redirect, request, session, url_for, flash
from cs50 import SQL
from flask_session import Session

app = Flask(__name__)

app.config["SESSION_PERMANET"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

db = SQL("sqlite:///shows.db")

@app.route("/")
def index():
    shows = db.execute("SELECT * FROM shows ORDER BY title")
    return render_template("index.html", shows=shows)

@app.route("/watch_list", methods=["POST", "GET"])
def watch_list():
    # if there is no watch_list dictionary then initiate an empty one
    if "watch_list" not in session:
        session["watch_list"] = []

    # add the movies to the watch list
    if request.method == "POST":
        show_id = request.form.get("id")
        if show_id:
            session["watch_list"].append(show_id)
        return redirect("/watch_list")
    
    if session["watch_list"]:
        shows = db.execute("SELECT * FROM shows WHERE id IN (?)", session["watch_list"])
    else:
        shows = []
    return render_template("watch_list.html", shows=shows)

    
        
