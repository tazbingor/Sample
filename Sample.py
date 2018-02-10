#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def hello_world():
    # return 'Hello World!'
    return render_template('index.html', title='Sample Blog')


@app.route('/services')
def services():
    return 'Service'


@app.route('/about')
def about():
    return 'About'


if __name__ == '__main__':
    # app.debug = True
    app.run(debug=True)
