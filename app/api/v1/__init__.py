from flask import Blueprint
from flask_restful import Api, Resource
from .views.UserView import DataParcel, SingleParcel, CancelOrder
from .views.AdminView import  admin_update_order_status

version1 = Blueprint('v1', __name__,  url_prefix = '/api/v1')

api = Api(version1)


##user routes
api.add_resource(DataParcel, '/parcels')
api.add_resource(SingleParcel, '/parcels/<order_id>')
api.add_resource(CancelOrder, '/parcels/<order_id>/cancel')

api.add_resource(admin_update_order_status, 'users/<user_id>/delivered')