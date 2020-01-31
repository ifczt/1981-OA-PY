from app.api.v1.token import auth
from app.libs.error_code import SuccessSQL, GET_SECTION_LIST, Success, ADD_SUCC
from app.libs.redprint import Redprint
from app.models.Section import Section
from app.models.base import db
from app.validators.forms import SectionForm, IDForm

api = Redprint('section')


@api.route('/list', methods=['get'])
def get_list():
    section_list = Section.query.filter_by().all()
    return SuccessSQL(msg=GET_SECTION_LIST, data=section_list)


@api.route('', methods=['post'])
@auth.login_required
def add_section():
    form = SectionForm().validate_for_api()
    _section = Section(name=form.name.data)
    db.session.add(_section)
    db.session.commit()
    return Success(msg=ADD_SUCC, data={'name': _section.name, 'id': _section.id})


@api.route('', methods=['put'])
@auth.login_required
def update_section():
    return Success()


@api.route('', methods=['delete'])
@auth.login_required
def del_section():
    form = IDForm().validate_for_api()
    _section = Section.query.filter_by(id=form.id.data).first()
    _section.delete()
    return Success()


