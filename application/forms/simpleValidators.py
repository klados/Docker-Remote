from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length


class DeleteImageForm(FlaskForm):
    imageId = StringField('imageId', validators=[DataRequired(), Length(min=71)])
    submit = SubmitField("Delete")
