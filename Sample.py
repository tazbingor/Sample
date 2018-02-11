#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import Flask, render_template
from werkzeug.routing import BaseConverter


class RegexConverter(BaseConverter):
    def __init__(self, url_map, *item):
        super(RegexConverter, self).__init__()


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


@app.route('/user/<int:user_id>')
def user(user_id):
    '''
    动态路由演示
    :param username:
    :return:
    '''
    return 'User %s' % user_id


if __name__ == '__main__':
    # app.debug = True
    app.run(debug=True)
