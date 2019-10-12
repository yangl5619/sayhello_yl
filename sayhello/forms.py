# -*- coding: utf-8 -*-
"""
    :author: Sam Yang (杨亮)
    :copyright: © 2019 Sam Yang 
    :license: MIT, see LICENSE for more details.
"""

from  flask_wtf import  FlaskForm
from  wtforms import  StringField, SubmitField, TextAreaField
from  wtforms.validators import  DataRequired, Length

class HelloForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired(), Length(1, 20)])
    body = TextAreaField('Message', validators=[DataRequired(), Length(1, 200)])
    submit = SubmitField()