import requests
import pytest
import json


@pytest.fixture()
def get_available_pets():
    def _method(name, category):
        headers = {
            'accept': 'application/json',
        }
        params = {
            'status': 'available'
        }
        response = requests.get('https://petstore.swagger.io/v2/pet/findByStatus', params=params, headers=headers)
        pets = json.loads(response.text)
        for pet in pets:
            if pet.get("name") == name and pet.get("category").get("name") == category:
                headers = {
                    'accept': 'application/json',
                    'Content-Type': 'application/json',
                }
                json_data = {
                    'id': 0,
                    'petId': 0,
                    'quantity': 0,
                    'status': 'placed',
                    'complete': True,
                }
                response = requests.post('https://petstore.swagger.io/v2/store/order', headers=headers, json=json_data)
                #return json.loads(response.text), 200
        else:
            return [], 400
    return _method
