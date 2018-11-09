import uuid
from werkzeug.security import generate_password_hash, check_password_hash

class Parcel(object):
	parcels = []
	def create_order(self,pickup_addr,destination_addr,item_type,recipient_name,recipient_id,weight,status):
		self.pickup_addr = pickup_addr
		self.destination_addr = destination_addr
		self.recipient_name = recipient_name
		self.recipient_id = recipient_id
		self.item_type = item_type
		self.weight = weight
		self.status = status

		payload  ={
		"order_id": str(uuid.uuid4().int),
		"pickup_address":self.pickup_addr,
		"destination_address":self.destination_addr,
		"recipient_name":self.recipient_name,
		"recipient_id":self.recipient_id,
		"item_type":self.item_type,
		"status":self.status
		}

		Parcel.parcels.append(payload)
		return True
	def get_all(self):
		"""Get all parcel orders
		return: """
		print(type(Parcel.parcels[0]["status"]))
		return Parcel.parcels

	def get_one_parcel(self,order_id):
		"""Gets a specific order with order_id as arguments
		param:order_id
		:return:"""
		
		for item in Parcel.parcels:
			if item["order_id"] == order_id:
				return item


	def cancel_order(self, order_id):
		for item in Parcel.parcels:
			if item["order_id"] == order_id:
				item['status'] = 'canceled'
				return True

class User_model(object):
	fields = []
	def create_user(self, email, username, password, con_password, role):
		self.email = email
		self.username = username 
		self.password = password
		self.con_password = con_password
		self.role = role


		payload={
			"user_id": str(uuid.uuid4().int),
			"email":self.email,
			"username":self.username,
			"password":self.password,
			"con_password":self.con_password,
			"role":self.role
		}
		User_model.fields.append(payload)
		return True

	def login_user(self, email, password, role):
		self.email = email
		self.password = password,
		self.role = role

		payload={
			"user_id":str(uuid.uuid4().int),
			"email":self.email,
			"password":self.password,
			"role":self.role
		}
		User_model.fields.append(payload)
		return True

	
	