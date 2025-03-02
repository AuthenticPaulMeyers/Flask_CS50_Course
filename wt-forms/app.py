from flask import Flask, render_template, redirect

from forms import FileForm

app = Flask(__name__)
app.config['SECRET_KEY']

@app.route('/')
def index():
    form = FileForm()
    return render_template('forms.html', form=form )