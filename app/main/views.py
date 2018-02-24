#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import render_template, flash, request
from . import main

@main.route('/')
def index():
    return render_template('index.html', title='Welcome')


@main.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404


@main.template_test('current_link')
def is_current_link(link):
    return link == request.path


@main.route('/user/<regex("[a-zA-Z]{3}"):user_id>/')
def user(user_id):
    return 'User %s' % user_id


@main.route('/services/')
def services():
    return 'Service'


@main.route('/about/')
def about():
    return 'About'


@main.route('/projects/')
@main.route('/works/')
@main.route('/our-works/')
def projects():
    '''
    多个路由响应一个方法
    :return:
    '''
    return 'The project page'

    # @app.route('/login/', methods=['GET', 'POST'])
    # def login():
    #     from app.auth.forms import LoginForm
    #     form = LoginForm()
    #     flash(u'登录成功!')
    #     return render_template('login.html', title=u'登录', form=form)

    # @app.route('/upload/', methods=['GET', 'POST'])
    # def upload():
    #     if request.method == 'POST':
    #         f = request.files['file']
    #         basepath = path.abspath(path.dirname(__file__))
    #         upload_path = path.join(basepath, 'static/uploads')
    #         f.save(upload_path, secure_filename(f.filename))
    #         return redirect(url_for('upload'))
    #
    #     return render_template('upload.html')
