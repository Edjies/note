# -*-coding:utf-8 -*-
from flask import render_template, url_for, redirect,request, flash
from flask_login import login_user, logout_user, login_required
from . import auth
from ..models import User
from .forms import LoginForm, RegistForm
from .. import db


@auth.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    # 提交登录
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        # 认证成功
        if user is not None and user.verify_password(form.password.data):
            #
            print("认证成功")
            # 保存用户状态
            login_user(user, form.remember_me.data)
            # 重定向到首页
            return redirect(request.args.get('next') or url_for('main.index'))
        # 认证失败
        else:
            flash('账号或密码错误')
    # 获取登录页面
    return render_template('auth/login.html', form=form)


@auth.route('/regist', methods=['GET', 'POST'])
def regist():
    form = RegistForm()
    if form.validate_on_submit():
        user = User(email=form.email.data, username=form.username.data, password=form.password.data)
        db.session.add(user)
        db.session.commit()
        flash("注册成功")
        return redirect(url_for('auth.login'))
    return render_template('auth/regist.html', form=form)


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    flash('您已经退出登录.')
    return redirect(url_for('main.index'))






