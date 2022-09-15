from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length


class ContactForm(FlaskForm):
    contact_name = StringField("Name", validators=[
        DataRequired(), Length(min=1, max=40)])
    contact_phonenumber = StringField("Phone", validators=[
        DataRequired(), Length(min=8, max=20)])
    submit = SubmitField("Save")
