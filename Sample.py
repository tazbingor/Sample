#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import Flask, render_template, request
from werkzeug.routing import BaseConverter


class RegexConverter(BaseConverter):
    def __init__(self, url_map, *items):
        super(RegexConverter, self).__init__(url_map)
        self.regex = items[0]


app = Flask(__name__)
app.url_map.converters['regex'] = RegexConverter


@app.route('/')
def hello_world():
    # return 'Hello World!'
    return render_template('index.html', title='Sample Blog')


# @app.route('/user/<int:user_id>')
# def user(user_id):
#     '''
#     动态路由演示
#     :param username:
#     :return:
#     '''
#     return 'User %s' % user_id


@app.route('/user/<regex("[a-zA-Z]{3}"):user_id>/')
def user(user_id):
    return 'User %s' % user_id


@app.route('/services/')
def services():
    return 'Service'


@app.route('/about/')
def about():
    return 'About'


@app.route('/projects/')
@app.route('/works/')
@app.route('/our-works/')
def projects():
    '''
    多个路由响应一个方法
    :return:
    '''
    return 'The project page'


@app.route('/login/', methods=['GET', 'POST'])
def login():
    return render_template('login.html', method=request.method)


if __name__ == '__main__':
    # app.debug = True
    app.run(debug=True)
