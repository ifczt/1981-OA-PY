"""
    Created by IFCZT on  2020/1/17 9:16
"""
__author__ = 'IFCZT'

import json
from datetime import datetime

from pip._vendor import requests

from app.config.setting import API_RATE_URL, API_RATE_DATA
from app.libs.error_code import SuccessSQL, GET_RATE, NotFound, RATE_NOT_FOUND
from app.libs.redprint import Redprint
from app.models.ExchangeRate import ExchangeRate
from app.models.User import User
from app.models.base import db
from app.validators.forms import RateForm

api = Redprint('exchange_rate')


@api.route('/list', methods=['get'])
def get_list():
    rate_list = ExchangeRate.query.all()
    return SuccessSQL(msg=GET_RATE, data=rate_list)


@api.route('', methods=['post'])
def get_single_rate():
    form = RateForm().validate_for_api()
    data = get_rate(form.scur.data, form.refresh.data)
    if not data:
        return NotFound(RATE_NOT_FOUND)
    return SuccessSQL(msg=GET_RATE, data=data)


def get_rate(scur, refresh=False):
    exchange = ExchangeRate.query.filter_by(currency_code=scur).first()
    day = datetime.now().day
    if exchange and not refresh:
        if exchange.update_time.day >= day:  # 当天不再从API获取汇率
            return exchange
    data = get_rate_api(scur)
    if exchange:
        ExchangeRate.query.filter_by(currency_code=scur).update(data)
        db.session.flush()
        db.session.commit()
    else:
        exchange = ExchangeRate(**data)
        db.session.add(exchange)
    return data


def get_rate_api(scur):
    API_RATE_DATA['scur'] = scur
    response = requests.post(API_RATE_URL, data=API_RATE_DATA)
    response = json.loads(response.text)
    data = {}
    if 'success' in response and response['success'] == '1':
        response = response['result']
        data['currency_code'] = response['scur']
        data['name'] = response['ratenm'].split('/')[0]
        data['rate'] = response['rate']
        data['update_time'] = response['update']
    return data
