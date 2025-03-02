from flask import Flask, request, render_template, redirect, url_for
from cs50 import SQL

app = Flask(__name__)

GENDER=["Male", "Female"]

# connect to the database
db = SQL("sqlite:///register.db")

@app.route("/")
def index():
    return render_template("index.html", gender=GENDER)

# registration route
@app.route("/register", methods=["POST", "GET"])
def add_students():
    firstname = request.form.get("firstname")
    middlename = request.form.get("middlename")
    lastname = request.form.get("lastname")
    gender = request.form.get("gender")
    date_of_birth = request.form.get("date_of_birth")
    email = request.form.get("email")
    phone = request.form.get("phone")

    if not firstname or not lastname or not gender or not email or not phone or not date_of_birth:
        return render_template("error.html", message="Required input can not be empty!")
    elif gender not in gender:
        return render_template("error.html", message="Invalid gender!")
    # insert the data into the database 
    db.execute("INSERT INTO students (firstname, middlename, lastname, gender, date_of_birth, email, phone) VALUES (?, ?, ?, ?, ?, ?, ?)", firstname, middlename, lastname, gender, date_of_birth, email, phone)
    return render_template("success.html", message="Student registered successfully!")

# Registrants
@app.route("/students")
def students_registered():
    students = db.execute("SELECT * FROM students")
    total = db.execute("SELECT COUNT(*) AS total_registrants FROM students")
    return render_template("register.html", students=students, total=total)

# update route
@app.route("/update/<int:student_id>", methods=["GET", "POST"])
def update(student_id):
    students = db.execute("SELECT id, firstname, middlename, lastname, gender, date_of_birth, email, phone FROM students WHERE id = ?", student_id)
    
    firstname = request.form.get("firstname")
    middlename = request.form.get("middlename")
    lastname = request.form.get("lastname")
    gender = request.form.get("gender")
    date_of_birth = request.form.get("date_of_birth")
    email = request.form.get("email")
    phone = request.form.get("phone")
    
    if request.method == 'POST':
        if not firstname or not lastname or not gender or not email or not phone or not date_of_birth:
            return render_template("error.html", message="Required input can not be empty!")
        elif gender not in gender:
            return render_template("error.html", message="Invalid gender!")
        
        db.execute("UPDATE students SET firstname = ? WHERE id = ?", firstname, student_id)
        db.execute("UPDATE students SET middlename = ? WHERE id = ?", middlename, student_id)
        db.execute("UPDATE students SET lastname = ? WHERE id = ?", lastname, student_id)
        db.execute("UPDATE students SET gender = ? WHERE id = ?", gender, student_id)
        db.execute("UPDATE students SET date_of_birth = ? WHERE id = ?", date_of_birth, student_id)
        db.execute("UPDATE students SET email = ? WHERE id = ?", email, student_id)
        db.execute("UPDATE students SET phone = ? WHERE id = ?", phone, student_id)
        return render_template("success.html", message="User updated successfully!")
    return render_template("update.html", students=students, gender=GENDER)



# delete route
@app.route("/delete/<int:student_id>")
def delete(student_id):
    db.execute("DELETE FROM students WHERE id = ?", student_id)
    return redirect(url_for("students_registered"))



    
    
