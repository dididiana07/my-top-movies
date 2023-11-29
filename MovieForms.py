from flask_wtf import FlaskForm
from wtforms.fields import StringField, SubmitField
from wtforms.validators import DataRequired


class AddMovie(FlaskForm):
    title = StringField(name="Title Movie", validators=[DataRequired()])
    director = StringField(name="Director", validators=[DataRequired()])
    rate = StringField(name="Rate (e.g. 7.5)", validators=[DataRequired()])
    description = StringField(name="Description", validators=[DataRequired()])
    opinion = StringField(name="Opinion", validators=[DataRequired()])
    image = StringField(name="URL Image", validators=[DataRequired()])
    submit = SubmitField("Submit")


class EditMovie(FlaskForm):
    rate = StringField(name="Rate (e.g. 7.5)")
    description = StringField(name="Description")
    opinion = StringField(name="Opinion")
    submit = SubmitField("Submit")