from ..models.AdminModels import UserOrders
from flask_restful import Resource
from flask import make_response, jsonify, request, abort

class admin_update_order_status(Resource):
	def put(self, user_id):
		user_id = str(user_id)
		order_1 = UserOrders()
		order_1.update_order_status(user_id)
		return make_response(jsonify({'message': 'order has been delivered!'}),200)

class admin_update_payment_status(Resource):
	def put(self, user_id):
		user_id = str(user_id)
		order_1 = UserOrders()
		order_1.update_order_payment(user_id)
		return make_response(jsonify({"message": "order paid!"}),200)