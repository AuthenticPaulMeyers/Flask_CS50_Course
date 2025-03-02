from flask import Flask, render_template, request, redirect, url_for
from cs50 import SQL

app = Flask(__name__)

STATUS = ["Done", "Not done"]
# connect to the database
db = SQL("sqlite:///todo.db")

# default route
@app.route("/")
def index():
    todolist = db.execute("SELECT * FROM todo")
    return render_template("index.html", todolist=todolist, status=STATUS)

# add todo route
@app.route("/add", methods=["POST", "GET"])
def add():
    title = request.form.get("title")
    status = request.form.get("status")

    if not title or not status:
        return render_template("error.html", message="Empty task or status!")
    # add task to the database 
    db.execute("INSERT INTO todo(title, status) VALUES (?, ?)", title, status)
    return redirect(url_for("index"))

# update task
@app.route("/update/<int:todo_id>")
def update(todo_id):
    db.execute("UPDATE todo SET status = 'Done' WHERE id = ?", todo_id)
    return redirect(url_for("index"))

# delete task
@app.route("/delete/<int:todo_id>")
def delete(todo_id):
    db.execute("DELETE FROM todo WHERE id = ?", todo_id)
    return redirect(url_for("index"))