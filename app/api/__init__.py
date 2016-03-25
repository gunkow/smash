from flask import Blueprint
from . import controllers
from flask.ext.restful import Api

api = Blueprint('api', __name__)
rest = Api(api)

rest.add_resource(controllers.Add, '/add/')

