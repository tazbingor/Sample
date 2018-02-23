#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import render_template, request, flash, redirect, url_for
from . import auth


@auth.route('/login/', methods=['GET', 'POST'])
def login():
    return render_template('login.html', title=u'登录', form=form)


@auth.route('/register/', methods=['GET', 'POST'])
def register():
    return render_template('register.html', title=u'注册')
