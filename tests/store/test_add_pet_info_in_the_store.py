import json

import pytest
import requests
import random


def test_add_pet_info_with_name_under_category():
    headers = {
        'accept': 'application/json'
    }

    json_data = {
        'id': random.randint(1000, 2000),
        'category': {
            'id': random.randint(2000, 3000),
            'name': 'Pomeranian',
        },
        'name': 'kurikuri',
        'photoUrls': [
            'string',
        ],
        'tags': [
            {
                'id': random.randint(3000, 4000),
                'name': 'string',
            },
        ],
        'status': 'available',
    }

    response = requests.post('https://petstore.swagger.io/v2/pet', headers=headers, json=json_data)
    print(response.text)
    resp = json.loads(response.text)
    assert response.status_code == 200

    with open("../../data/add_pet_info.json", "w+") as json_file:
        json_file.write(response.text)
