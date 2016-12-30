# -*-coding:utf-8 -*-
from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, PasswordField, SubmitField, ValidationError
from wtforms.validators import DataRequired, Length, Email, Regexp, EqualTo

from ..models import User


class LoginForm(FlaskForm):
    email = StringField('email', validators=[DataRequired(), Length(1, 64), Email()])
    password = PasswordField('password', validators=[DataRequired()])
    remember_me = BooleanField('keep me logged in')
    submit = SubmitField('登录')


class RegistForm(FlaskForm):
    email = StringField('email', validators=[DataRequired(), Length(1, 64), Email()])
    username = StringField('username', validators=[DataRequired(), Regexp('^[A-Za-z][A-Za-z0-9_.]*$', 0, '用户名必须只能包含 字母， 数字， 下划线 和 小数点')])
    password = PasswordField('password', validators=[DataRequired(), EqualTo('password2', '密码必须一致')])
    password2 = PasswordField('password2', validators=[DataRequired()])
    regist = SubmitField('注册')

    def validate_email(self, field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError('邮箱已被注册')

    def validate_username(self, field):
        if User.query.filter_by(username=field.data).first():
            raise  ValidationError('用户名已被注册')
