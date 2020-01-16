"""
    Created by IFCZT on  2020/1/8 15:17
"""
from .app import Flask
from flask_cors import *
__author__ = 'IFCZT'

def register_blueprints(_app):
    from app.api.v1 import create_blueprint
    _app.register_blueprint(create_blueprint())


def register_plugin(_app):
    from app.models.base import db
    db.init_app(_app)
    with _app.app_context():
        db.create_all()



def create_app():
    app = Flask(__name__)
    CORS(app)
    app.config.from_object('app.config.setting')
    app.config.from_object('app.config.secure')

    register_blueprints(app)
    register_plugin(app)
    return app
