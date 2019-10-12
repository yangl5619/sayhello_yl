# -*- coding: utf-8 -*-
"""
    :author: Sam Yang (杨亮)
    :copyright: © 2019 Sam Yang 
    :license: MIT, see LICENSE for more details.
"""
from  flask import  flash, redirect, url_for, render_template

from sayhello import  app, db
from sayhello.forms import HelloForm
from sayhello.models import Message

@app.route('/', methods=['GET', 'POST'])
def index():
    messages = Message.query.order_by(Message.timestamp.desc()).all()
    form = HelloForm()
    if form.validate_on_submit():
        name = form.name.data
        body = form.body.data
        message = Message(body=body, name=name)
        db.session.add(message)
        db.session.commit()
        flash('Your message have been sent to you world!')
        return redirect('index.html')
    return render_template('index.html', form=form, messages=messages)