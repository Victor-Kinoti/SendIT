from flask import Blueprint
from flask_restful import Api, Resource
from .views.UserViews import DataParcel, SingleParcel, CancelOrder, RegisterUser,UserLogin
from .views.AdminView import  admin_update_order_status,admin_update_payment_status,Admin_user_all_Order

version1 = Blueprint('v1', __name__,  url_prefix = '/api/v1')

api = Api(version1)


##user routes
api.add_resource(DataParcel, '/parcels')
api.add_resource(SingleParcel, '/parcels/<order_id>')
api.add_resource(CancelOrder, '/parcels/<order_id>/cancel')
api.add_resource(RegisterUser, "/register")
api.add_resource(UserLogin, '/login')
##admin routes
api.add_resource(Admin_user_all_Order, '/users/<user_id>/parcels')
api.add_resource(admin_update_payment_status, 'users/<user_id>/paid')
api.add_resource(admin_update_order_status, 'users/<user_id>/delivered')