#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import Flask, render_template, request, redirect, url_for, make_response, abort
from werkzeug.routing import BaseConverter
from werkzeug.utils import secure_filename
from flask_script import Manager
from os import path

from flask_bootstrap import Bootstrap
from flask_nav import Nav
from flask_nav.elements import *


class RegexConverter(BaseConverter):
    def __init__(self, url_map, *items):
        '''
        初始化regex解析URL
        :param url_map:
        :param items:
        '''
        super(RegexConverter, self).__init__(url_map)
        self.regex = items[0]


app = Flask(__name__)
app.url_map.converters['regex'] = RegexConverter
Bootstrap(app)
nav = Nav()
app.config.from_pyfile('config')
manager = Manager(app)

nav.register_element('top', Navbar(u'Flask入门',
                                   View(u'主页', 'index'),
                                   View(u'关于', 'about'),
                                   View(u'服务', 'services'),
                                   View(u'项目', 'projects')))

nav.init_app(app)


@app.route('/')
def index():
    response = make_response(render_template('index.html', title='Welcome'))
    response.set_cookie('username', 'te')
    return response


@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404


@manager.command
def dev():
    from livereload import Server
    live_server = Server(app.wsgi_app)
    live_server.watch('**/*.*')
    live_server.serve(open_url=True)


@app.template_test('current_link')
def is_current_link(link):
    return link == request.path


# @app.route('/')
# def hello_world():
#     # return 'Hello World!'
#     return render_template('index.html', title='Sample Blog')


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
    from forms import LoginForm
    form = LoginForm()
    return render_template('login.html', title='Login', form=form)


@app.route('/upload/', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        f = request.files['file']
        basepath = path.abspath(path.dirname(__file__))
        upload_path = path.join(basepath, 'static/uploads')
        f.save(upload_path, secure_filename(f.filename))
        return redirect(url_for('upload'))

    return render_template('upload.html')


if __name__ == '__main__':
    # app.debug = True
    # app.run(debug=True)
    # manager.run()
    dev()
