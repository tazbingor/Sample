#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import render_template, redirect, make_response, flash, request


def init_views(app):
    @app.route('/')
    def index():
        return render_template('index.html', title='Welcome')

    @app.errorhandler(404)
    def page_not_found(error):
        return render_template('404.html'), 404

    @app.template_test('current_link')
    def is_current_link(link):
        return link == request.path

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
        from app.forms import LoginForm
        form = LoginForm()
        flash(u'登录成功!')
        return render_template('login.html', title=u'登录', form=form)

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
