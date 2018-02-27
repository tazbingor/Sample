#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import Flask
from os import path
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

basedir = path.abspath(path.dirname(__file__))
db = SQLAlchemy
bootstrap = Bootstrap()
login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'auth.login'


def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('config')
    app.config['SQLALCHEMY_DATABASE_URI'] = \
        'sqlite:///' + path.join(basedir, 'data.sqlite')
    app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True

    db.init_app(app)
    bootstrap.init_app(app)
    login_manager.init_app(app)


    from auth import auth as  auth_blueprint
    from main import main as  main_blueprint

    app.register_blueprint(auth_blueprint, url_prefix='/auth')
    app.register_blueprint(main_blueprint, static_folder='static')

    return app
