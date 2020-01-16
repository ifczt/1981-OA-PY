"""
    Created by IFCZT on  2020/1/8 15:36
"""
__author__ = 'IFCZT'

# region MySql Config
DIALECT = 'mysql'
DRIVER = 'mysqlconnector'
USERNAME = 'root'
PASSWORD = '123123'
HOST = '127.0.0.1'
PORT = '3306'
DATABASE = '1981'
SQLALCHEMY_DATABASE_URI = '{}+{}://{}:{}@{}:{}/{}?charset=utf8&auth_plugin=mysql_native_password'.format(
    DIALECT, DRIVER, USERNAME, PASSWORD, HOST, PORT, DATABASE
)
# 是否自动提交 需要即时取id的地方 得先commit
SQLALCHEMY_COMMIT_ON_TEARDOWN = True
SQLALCHEMY_TRACK_MODIFICATIONS = False
# endregion
SECRET_KEY = 'IＬＯＶＥ：ＩＦＣＺＴ'
