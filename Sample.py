#!/usr/bin/env python
# -*- coding: utf-8 -*-
from os import path

from flask import Flask, render_template, redirect, make_response, flash
from flask_bootstrap import Bootstrap
from flask_nav import Nav
from flask_nav.elements import *
from flask_script import Manager
from flask_sqlalchemy import SQLAlchemy
from werkzeug.routing import BaseConverter
from werkzeug.utils import secure_filename


class RegexConverter(BaseConverter):
    def __init__(self, url_map, *items):
        '''
        初始化regex解析URL
        :param url_map:
        :param items:
        '''
        super(RegexConverter, self).__init__(url_map)
        self.regex = items[0]


basedir = path.abspath(path.dirname(__file__))

db = SQLAlchemy()
bootstrap = Bootstrap()
nav = Nav()
# manager = Manager(app) # 管理员


def create_app():
    app = Flask(__name__)
    app.url_map.converters['regex'] = RegexConverter
    app.config.from_pyfile('config')  # CSRF配置文件
    # 数据库关联
    app.config['SQLALCHEMY_DATABASE_URI'] = \
        'sqlite:////' + path.join(basedir, 'data.sqlite')
    app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True

    nav.register_element('top', Navbar(u'Flask入门',
                                       View(u'主页', 'index'),
                                       View(u'关于', 'about'),
                                       View(u'服务', 'services'),
                                       View(u'项目', 'projects')))
    db.init_app(app)
    bootstrap.init_app(app)
    nav.init_app(app)

    return app


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


@app.route('/upload/', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        f = request.files['file']
        basepath = path.abspath(path.dirname(__file__))
        upload_path = path.join(basepath, 'static/uploads')
        f.save(upload_path, secure_filename(f.filename))
        return redirect(url_for('upload'))

    return render_template('upload.html')


class Role(db.Model):
    __tablename__ = 'roles'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=True)
    users = db.relationship('User', backref='roles')  # 指向当前的表


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=True)
    password = db.Column(db.String, nullable=True)
    role_id = db.Column(db.String, db.ForeignKey('roles.id'))  # 指向roles.id


# if __name__ == '__main__':
#     # app.debug = True
#     # app.run(debug=True)
#     # manager.run()
#     dev()
