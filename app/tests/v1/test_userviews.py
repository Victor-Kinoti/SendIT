import unittest
import json
from ... import create_app
from ...api.v1.views import UserViews
from ...api.v1.models.UserModels import Parcel

class ParcelModelCase(unittest.TestCase):
    def setUp(self):
        
        self.app = create_app()
        self.client = self.app.test_client()
        self.app_context = self.app.app_context()
        self.app_context.push()

        self.order_1 = json.dumps({"destination_address":"Nairobi", "pickup_address":"Kisumu", 
        "recipient_name":"keynote", "recipient_id":"316459", "item_type":"parcel", "weight":"65kg", 
        "status":"canceled"})
        self.order_2 = json.dumps({
            "username":"Keynote", "email":"vik@gmail.com", "password":"pass", "con_password":"pass", "role":"admin"
        })
        self.order_3 = json.dumps({
            "username":"Keynote", "email":"vik@gmail.com", "password":"pass", "con_password":"password", "role":"admin"
        })

        self.order_4 = json.dumps({
             "email":"vik@gmail.com", "password":"pass", "con_password":"password", "role":"admin"
        })

        self.order_5 = json.dumps({
            "username":"Keynote", "email":"vik@gmail.com", "con_password":"password", "role":"admin"
        })

        self.order_6 = json.dumps({
            "email":"vik@gmail.com", "password":"password", "role":"admin"
        })

    def test_create_order(self):
        res = self.client.post('/api/v1/parcels', data=self.order_1, content_type='application/json')
        output = json.loads(res.data.decode())
        self.assertEqual(output['Status'], "created", msg="Incomplete credentials not allowed")
        assert res.status_code == 201

    def test_get_all_orders(self):
        res = self.client.get('/api/v1/parcels')

        self.assertTrue(res.status_code, 200)

    def test_cancel_order(self):
        res = self.client.put('/api/v1/parcels/1/cancel', data=self.order_1, content_type='application/json')
        output = json.loads(res.data.decode())
        assert res.status_code == 201
        self.assertEqual(output['Status'], 'order has been canceled')

    def test_register_user(self):
        res = self.client.post("/api/v1/register", data=self.order_2, content_type='application/json')
        output = json.loads(res.data.decode())
        assert res.status_code == 201
        assert res.content_type == 'application/json;charset=utf-8'
        assert output['Status'] == 'created'

    def test_pass_not_matching(self):
        res = self.client.post("/api/v1/register", data=self.order_3, content_type='application/json')
        output = json.loads(res.data.decode())
        assert output['message'] == "Password and confirm password not matching"
        assert res.content_type == 'application/json'
        assert res.status_code == 400

    def test_username_missing(self):
        res = self.client.post("/api/v1/register", data=self.order_4, content_type='application/json')
        output = json.loads(res.data.decode())
        assert output['message'] == "Username missing"
        assert res.content_type == 'application/json'
        assert res.status_code == 400
        
    def test_password_missing(self):
        res = self.client.post("/api/v1/register", data=self.order_5, content_type='application/json')
        output = json.loads(res.data.decode())
        assert res.content_type == 'application/json'
        assert output['message'] == "Password missing"
        assert res.status_code == 400

    def test_user_login(self):
        res = self.client.post("/api/v1/login", data=self.order_6, content_type='application/json')
        output = json.loads(res.data.decode())
        assert output['Status'] == 'created'
        assert res.status_code == 201
        assert res.content_type == 'application/json;charset=utf-8'


if __name__ == '__main__':
    unittest.main()