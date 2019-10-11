# -*- coding: utf-8 -*-
"""
    :author: Sam Yang (杨亮)
    :copyright: © 2019 Sam Yang 
    :license: MIT, see LICENSE for more details.
"""
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask('sayhello')
app.config.from_pyfile('settings.py')
app.jinja_env.trim_blocks = True
app.jinja_env.lstrip_blocks = True

db = SQLAlchemy(app)

from sayhello import views, errors, commands