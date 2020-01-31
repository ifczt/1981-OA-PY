"""
    Created by IFCZT on  2020/1/16 14:02
"""
__author__ = 'IFCZT'

import time

from flask import request, g

from app.models.LoginLog import LoginLog
from app.models.base import db


def insert_log(u_id):
    data = {'u_id': u_id, 'ip': request.remote_addr}
    # hour = time.localtime().tm_hour
    log = LoginLog(**data)
    db.session.add(log)
