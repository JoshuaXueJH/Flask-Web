from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField, TextAreaField
from flask_pagedown.fields import PageDownField
from wtforms.validators import Required


class PostForm(FlaskForm):
    post = PageDownField("What's on your mind?", validators=[Required()])
    submit = SubmitField('Submit')
