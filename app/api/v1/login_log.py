"""
    Created by IFCZT on  2020/1/16 14:02
"""
__author__ = 'IFCZT'

from flask import request

from app.models.LoginLog import LoginLog
from app.models.base import db


def insert_log(u_id):
    log = LoginLog(u_id=u_id, ip=request.remote_addr)
    db.session.add(log)
