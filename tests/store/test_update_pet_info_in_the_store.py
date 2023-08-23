import json
import pytest
import requests


def test_add_pet_info_with_name_under_category():
    with open("../../data/add_pet_info.json", "r") as json_file:
        json_object = json.load(json_file)

    headers = {
        'accept': 'application/json'
    }
    json_object["tags"][0]["name"] = "Super Cute"
    response = requests.put('https://petstore.swagger.io/v2/pet', headers=headers, json=(json_object))

    resp = json.loads(response.text)
    assert response.status_code == 200

    with open("../../data/update_pet_info.json", "w+") as json_file:
        json_file.write(response.text)
