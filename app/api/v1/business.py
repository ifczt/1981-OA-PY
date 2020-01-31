from flask import request, g

from app.api.v1.token import auth
from app.libs.error_code import Success
from app.libs.redprint import Redprint
from app.models.Business import Business
from app.models.LoginLog import LoginLog
from app.models.base import db
from app.validators.forms import ProductForm

api = Redprint('business')


# region 添加产品
@api.route('', methods=['post'])
@auth.login_required
def add_product():
    form = ProductForm().validate_for_api()
    db.session.add(Business(u_id=form.u_id.data, product=form.product.data, url=form.url.data))
    return Success()
# endregion
