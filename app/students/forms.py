
from flask_wtf import FlaskForm
from wtforms import StringField, SelectField
from wtforms.validators import DataRequired
from app.models import  Track, Student
from wtforms_sqlalchemy.fields import QuerySelectField

def enabled_tracks():
    return Track.query.all()
class StudentForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    image = StringField('Image')
    # track = QuerySelectField('Track', query_factory=enabled_tracks)



# class StudentForm()

from wtforms_sqlalchemy.orm import model_form
StudentModelForm = model_form(Student)

