"""
    Created by IFCZT on  2020/1/8 16:48
"""
from app.libs.error_code import PARAM_REQUIRE, PARAM_FAILED, PARAM_LENGTH

__author__ = 'IFCZT'
from wtforms.validators import DataRequired as dataRequired, Regexp as regexp, Length as length


class DataRequired(dataRequired):
    def __init__(self, message=PARAM_REQUIRE):
        self.message = message


class Regexp(regexp):
    def __init__(self, regex, flags=0, message=PARAM_FAILED):
        super().__init__(regex, flags, message)

class Length(length):
    def __init__(self, min=-1, max=-1, message=PARAM_LENGTH):
        super().__init__(min,max,message)
