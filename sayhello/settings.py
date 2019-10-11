# -*- coding: utf-8 -*-
"""
    :author: Sam Yang (杨亮)
    :copyright: © 2019 Sam Yang 
    :license: MIT, see LICENSE for more details.
"""

import os
import sys

from sayhello import  app

WIN = sys.platform.startswith('win')

if WIN:
    prefix = 'sqlite:///'
else:
    prefix = 'sqlite:////'

dev_db = prefix + os.path.join(os.path.dirname(app.root_path), 'data.db')
SECRET_KEY = os.getenv('SECRET_KEY', 'secret string')
SQLALCHEMY_TRACK_MODIFICATIONS = False
SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URI', dev_db)