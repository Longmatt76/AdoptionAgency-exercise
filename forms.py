from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, IntegerField
from wtforms.validators import InputRequired, Optional, URL, NumberRange, Length


class PetForm(FlaskForm):
    """form for adding new pet"""
    name = StringField('Pet Name:', validators=[InputRequired()])
    species = SelectField('Species:', choices=[('cat','cat'),('dog','dog'),('porcupine','porcupine')] ,validators=[InputRequired()])
    photo_url = StringField('Photo Url:',validators=[Optional(),URL()])
    age = IntegerField('Age:', validators=[NumberRange(min=0,max=30,message='Age must be between 0 and 30'),Optional()])
    notes = StringField('Notes:')
