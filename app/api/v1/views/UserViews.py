from ..models.UserModels import Parcel, User_model
from flask_restful import Resource
from flask import make_response, jsonify, request, abort
from email.utils import parseaddr

class DataParcel(Resource):
	"""Utilizes data from an order by either getting all data or posting new data"""
	def post(self):
		
		data = request.get_json() or {}

		
		if 'destination_address' not in data:
			abort(make_response(jsonify(message="destination_address missing"),400))
		if 'pickup_address' not in data:
			abort(make_response(jsonify(message="pickup_address missing"),400))
		if 'recipient_name' not in data:
			abort(make_response(jsonify(message="recipient_name missing"),400))
		if 'recipient_id' not in data:
			abort(make_response(jsonify(message="recipient_id missing"),400))
		if 'item_type' not in data:
			abort(make_response(jsonify(message="item_type missing"),400))
		if 'weight' not in data:
			abort(make_response(jsonify(message="weight missing"),400))	
		if 'status' not in data:
			abort(make_response(jsonify(message="status missing"),400))	
		if len(data)==0:
			abort(make_response(jsonify(message="Fill in the fields"),400))

		par = Parcel()
		par.create_order(
			data["destination_address"],
			data["pickup_address"],
			data["recipient_name"],
			data["recipient_id"],
			data["item_type"],
			data["weight"],
			data["status"]
			)

		payload = {
			"Status":"created",
			
		}
		result= make_response(jsonify(payload), 201)
		result.content_type = 'application/json;charset=utf-8'
		return result

	def get(self):
		"""gets all orders made"""
		par = Parcel()
		all_orders = par.get_all()
		

		payload = {
			"Status":"Ok",
			"Parcels": all_orders
		}
		return make_response(jsonify(payload),201)

class SingleParcel(Resource):


	def get(self, order_id):
		order_id = str(order_id)
		par = Parcel()
		one_order = par.get_one_parcel(order_id)
		if one_order:
			payload = {
				"Status":"Ok",
				"Parcels": one_order
			}
		else:
			abort(make_response(jsonify(message="Not found")))
		
		res= make_response(jsonify(payload))
		if res.content_type != 'application/json':
			abort(make_response(jsonify(message="Not json format")))
		res.content_type = 'application/json;charset=utf-8'
		return res

class CancelOrder(Resource):

	def put(self, order_id):
		order_id = str(order_id)
		order_1 = Parcel()
		order_1.cancel_order(order_id)
		return make_response(jsonify({'Status': 'order has been canceled'}),201)

class UserLogin(Resource):
	def post(self):
		

		data = request.get_json()
		if 'email' not in data:
			abort(make_response(jsonify(message="Email missing"),400))
		if 'password' not in data:
			abort(make_response(jsonify(message="Password missing"),400))
		if 'role' not in data:
			abort(make_response(jsonify(message="Please check a role"),400))
		if len(data)==0:
			abort(make_response(jsonify(message="Fill in the fields"),400))

		user_1 = User_model()
		user_1.login_user(
			data["email"],
			data["password"],
			data["role"]
			)

		payload = {
			"Status":"created",
			
		}
		result= make_response(jsonify(payload), 201)
		if result.content_type == 'application/json;charset=utf-8':
			return result
		return make_response(jsonify({"Status": "Wrong Content!!"}))
class RegisterUser(Resource):
	def post(self):		
			
		data = request.get_json() or {}
		if 'username' not in data:
			abort(make_response(jsonify(message="Username missing"),400))
		if 'email' not in data:
			abort(make_response(jsonify(message="Email missing"),400))
		if 'con_password' not in data:
			abort(make_response(jsonify(message="Confirmation password missing"),400))
		if 'password' not in data:
			abort(make_response(jsonify(message="Password missing"),400))
		if 'role' not in data:
			abort(make_response(jsonify(message="Please check a role"),400))

		if data['password'] != data['con_password']:
			abort(make_response(jsonify(message="Password and confirm password not matching"),400))
		if '@' in parseaddr(data['email']):
			abort(make_response(jsonify(message="wrong email format"),400))
			
		if len(data)==0:
			abort(make_response(jsonify(message="Fill in the fields"),400))
		
		user_1 = User_model()
		user_1.create_user(
			data["username"],
			data["email"],
			data["password"],
			data["con_password"],
			data["role"]
			)

		payload = {
			"Status":"created",
			
		}
		result= make_response(jsonify(payload), 201)
		result.content_type = 'application/json;charset=utf-8'
		return result
