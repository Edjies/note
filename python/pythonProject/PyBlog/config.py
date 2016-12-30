# -*-coding:utf-8 -*-
import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    SECRET_KEY = 'phb918151'                #
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True    #
    MYBLOG_MAIL_SUBJECT_PREFIX= '[Flasky]'
    MYBLOG_MAIL_SENDER = 'Flasky Admin <flasky @ example.com > '
    MYBLOG_ADMIN = 'panhaobo1991@193.com'

    @staticmethod
    def init_app(app):
        pass


class DevConfig(Config):
    DEBUG = True
    MAIL_SERVER = 'panhaobo1991@163.com'
    MAIL_PORT = '9999'
    MAIL_USR_TLS = True
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'data-dev.sqlite')


class TestConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'data-test.sqlite')


class ProConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'data-pro.sqlite')


config = {
    'dev': DevConfig,
    'test': TestConfig,
    'pro': ProConfig,
    'default': DevConfig
}


