"""
 Created by 七月 on 2018/5/7.
"""
from .app import Flask
from flask_migrate import Migrate, MigrateCommand
from app.api.restaurant.models import shoppingCart, menu, foodOrder,orderItem, user


__author__ = '七月'


def register_blueprints(app):
    from app.api.restaurant.v1 import create_blueprint_v1
    #from app.web import create_blueprint_web
    #app.register_blueprint(create_blueprint_v1(),
                           #url_prefix='/resturant/v1', subdomain='api')
    #app.register_blueprint(create_blueprint_web())
    app.register_blueprint(create_blueprint_v1(),
                           url_prefix='/resturant/v1')



def register_plugin(app):
    from app.libs.model_base import db
    db.init_app(app)
    migrate = Migrate(app, db)

    # 使用migrate 不需要重复db.create_all()
    #with app.app_context():
    #    db.create_all()



# 解决跨域
def apply_cors(app):
    from flask_cors import CORS
    CORS(app)


def apply_email(app):
    from app.libs.email import mail
    mail.init_app(app)


def create_app():
    #app = Flask(__name__, static_url_path='', subdomain_matching=True)
    # app.url_map.default_subdomain = 'www'
    app = Flask(__name__)
    app.config.from_object('app.config.setting')
    app.config.from_object('app.config.secure')

    apply_cors(app)
    register_blueprints(app)
    register_plugin(app)
    apply_email(app)
    app.view_functions
    print(app.url_map)


    app.logger.info("\n\n %s", dog_log)
    return app


dog_log = """
            ─────────▄──────────────▄────
            ─ wow ──▌▒█───────────▄▀▒▌───
            ──▐▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▀▀────────
          """
