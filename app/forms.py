from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import Email, DataRequired


class LoginForm(FlaskForm):
    #field name = datatypeField('LABEL', validators=[LIST OF validators])
    pokemon = StringField('Pokemon', validators=[DataRequired()])
    submit = SubmitField('Login')