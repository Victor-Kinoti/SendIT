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
