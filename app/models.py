#!/usr/bin/env python
# -*- coding: utf-8 -*-
from . import db


class Role(db.Model):
    __tablename__ = 'roles'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=True)
    users = db.relationship('User', backref='role')  # 指向当前的表

    @staticmethod
    def seed():
        db.session.add_all(map(lambda r: Role(name=r), ['Guests', 'Administrators']))
        db.session.commit()


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=True)
    password = db.Column(db.String, nullable=True)
    role_id = db.Column(db.String, db.ForeignKey('roles.id'))  # 指向roles.id

    @staticmethod
    def on_created(target, value, initiator):
        target.role = Role.query.filter_by(name='Guests').first()


db.event.listen(User.name, 'set', User.on_created)


@db.user_loader
def get_user(user_id):
    return User.query.filter_by(name=user_id).first()
