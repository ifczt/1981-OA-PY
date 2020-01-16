"""
 Created by 七月 on 2018/5/12.
"""
from flask import request, json
from werkzeug.exceptions import HTTPException

__author__ = '七月'


class APIException(HTTPException):
    code = 500
    msg = '抱歉，我们引起了一个错误！o(╯□╰)o'
    data = None
    def __init__(self, msg=None, code=None,data=None):
        if code:
            self.code = code
        if msg:
            self.msg = msg
        if data:
            self.data = data
        super(APIException, self).__init__(msg, None)

    def get_body(self, environ=None):
        body = dict(
            msg=self.msg,
            code=self.code,
            request=request.method + ' ' + self.get_url_no_param()
        )
        text = json.dumps(body)
        return text

    def get_headers(self, environ=None):
        return [('Content-Type', 'application/json')]

    @staticmethod
    def get_url_no_param():
        full_path = str(request.full_path)
        main_path = full_path.split('?')
        return main_path[0]

