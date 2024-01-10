from flask import Blueprint
from controllers.users import users_blueprint
from controllers.rooms import rooms_blueprint
from controllers.message import message_blueprint
from controllers.participants import participants_blueprint


routes = Blueprint('routes', __name__, url_prefix='/api/v1')

routes.register_blueprint(users_blueprint)
routes.register_blueprint(rooms_blueprint)
routes.register_blueprint(message_blueprint)
routes.register_blueprint(participants_blueprint)
