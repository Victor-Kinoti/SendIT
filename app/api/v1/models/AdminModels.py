import uuid

class UserOrders(object):
    orders = [{
        "user_id":str(uuid.uuid4().int),
        "pickup_address":"Nairobi",
        "destination_address":"Meru",
        "order_type":"Parcel",
        "payment_status":"Not Paid",
        "order_status":"Delivered",


    },
    {
        "user_id":str(uuid.uuid4().int),
        "pickup_address":"Naivasha",
        "destination_address":"Thika",
        "order_type":"Envelope",
        "payment_status":"Paid",
        "order_status":"Delivered",


    },
    {
        "user_id":str(uuid.uuid4().int),
        "pickup_address":"Mombasa",
        "destination_address":"Nakuru",
        "order_type":"Parcel",
        "payment_status":"Paid",
        "order_status":"InTransit",


    }]


    def update_order_status(self, user_id):
        for item in UserOrders.orders:
            if item["user_id"] == user_id:
                item['status'] == 'Delivered'
                return True