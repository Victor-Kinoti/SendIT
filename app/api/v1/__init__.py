from flask import Blueprint
from flask_restful import Api, Resource
from .views.UserView import DataParcel, SingleParcel

version1 = Blueprint('v1', __name__,  url_prefix = '/api/v1')

api = Api(version1)


##user routes
api.add_resource(DataParcel, '/parcels')
api.add_resource(SingleParcel, '/parcels/<order_id>')