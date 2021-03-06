"""
    Created by IFCZT on  2020/1/8 15:49
"""
from flask import request
from wtforms import Form

from app.libs.error_code import ParameterException

__author__ = 'IFCZT'


class BaseForm(Form):
    def __init__(self):
        data = request.get_json(silent=True)
        args = request.args.to_dict()
        super(BaseForm, self).__init__(data=data, **args)

    def validate_for_api(self):
        valid = super(BaseForm, self).validate()
        if not valid:
            raise ParameterException(msg=self.errors)
        return self
