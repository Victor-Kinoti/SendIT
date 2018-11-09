from ..models.AdminModels import UserOrders
from flask_restful import Resource
from flask import make_response, jsonify, request, abort

class Admin_all_Orders(Resource):
	def get(self):
		"""gets all orders made"""
		order_1 = UserOrders()
		all_orders = order_1.get_all_orders()
		

		payload = {
			"Status":"Ok",
			"Parcels": all_orders
		}
		result= make_response(jsonify(payload),200)
		result.content_type = 'application/json;charset=utf-8'
		return result

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

class Admin_user_all_Order(Resource):
	def get(self, user_id):
		user_id = str(user_id)
		order_1 = UserOrders()
		one_order = order_1.get_one_user_order(user_id)
		if one_order:
			payload = {
				"Status":"Ok",
				"Parcels": one_order
			}
		else:
			abort(make_response(jsonify(message="Not found")),404)
		
		result= make_response(jsonify(payload))
		if result.content_type != 'application/json':
			abort(make_response(jsonify(message="Not json format")),404)
		result.content_type = 'application/json;charset=utf-8'
		return result