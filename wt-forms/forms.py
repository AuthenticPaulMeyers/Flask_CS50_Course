from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired

class FileForm(FlaskForm):
    file = FileField("File", validators=[FileRequired()])