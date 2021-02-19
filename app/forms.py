from flask_wtf import FlaskForm
from wtforms import StringField, validators, TextAreaField, SubmitField


class ContactForm(FlaskForm):
    name = StringField('Name',[validators.DataRequired()])

    email = StringField('Email Address', [validators.DataRequired(), validators.Email(), validators.Length(min=6, max=35)])

    subject = StringField('Subject',[validators.DataRequired()])

    message = TextAreaField('Message',[validators.DataRequired()])

    submit = SubmitField('Send')
