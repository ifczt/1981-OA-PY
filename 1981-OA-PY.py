"""
    Created by IFCZT on  2020/1/8 15:12
"""
from werkzeug.exceptions import HTTPException

from app import create_app
from app.config.setting import DEBUG
from app.libs.error import APIException
from app.libs.error_code import ServerError, URL_NOT_EXISTS

__author__ = 'IFCZT'

app = create_app()


@app.errorhandler(Exception)
def framework_error(e):
    if isinstance(e, APIException):
        return e
    if isinstance(e, HTTPException):
        code = e.code
        msg = URL_NOT_EXISTS if code ==  404 else e.description
        return APIException(msg, code)
    else:
        if not DEBUG:
            return ServerError()
        else:
            raise e

if __name__ == '__main__':
    app.run(debug=True)
