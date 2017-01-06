# -*-coding:utf-8 -*-
from . import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask import current_app
from flask_login import UserMixin
from . import login_manager
from datetime import datetime


class Permission:
    FOLLOW = 0x01  # 关注用户  0b00000001
    COMMENT = 0x02 # 发布评论  0b00000010
    WRITE_ARTICLES = 0x04 # 写文章 0b0000010
    ADMIN = 0x80  # 管理网站


class Role(db.Model):

    __tablename__ = 'roles'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    permissions = db.Column(db.Integer)
    users = db.relationship('User', backref='role')

    def __init__(self, name, permissions):
        self.name = name
        self.permissions = permissions

    @staticmethod
    def init_roles():
        roles = {
            'User': (Permission.FOLLOW | Permission.COMMENT | Permission.WRITE_ARTICLES,),
            'Admin': (Permission.FOLLOW | Permission.COMMENT | Permission.WRITE_ARTICLES | Permission.ADMIN,)
        }
        for role in roles:
            # 如果没有在数据库中找到，则插入
            r = Role.query.filter_by(name=role).first()
            if r is None:
                db.session.add(Role(role, roles[role][0]))
        db.session.commit()

    def __repr__(self):
        return '<Role % r, % d>' % (self.name, self.permissions)


class User(db.Model, UserMixin):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(64), unique=True, index=True)
    username = db.Column(db.String(64), unique=True, index=True)
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))
    password_hash = db.Column(db.String(128))
    posts = db.relationship('Post', backref='author', lazy='dynamic')

    def __init__(self, email='', username='', password='123456'):
        self.email = email
        self.username = username
        self.password = password
        if self.role is None:
            if self.email == current_app.config['MYBLOG_ADMIN']:
                self.role = Role.query.filter_by(permissions=0xff).first()
            if self.role is None:
                self.role = Role.query.filter_by(permissions=0x07).first()

    @property
    def password(self):
        raise AttributeError('password is not a readable attribute')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return '<User % r, %r>' % (self.username, self.email)


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class Post(db.Model):
    __tablename__='posts'
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.Text)
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    author_id = db.Column(db.Integer, db.foreignKey('users.id'))



class ClassC(db.Model):
    pass

p = Post(a='a')
c = ClassC(author='c')

