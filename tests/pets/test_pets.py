import pytest

from libs.utils import get_available_pets
import requests


# @pytest.mark.parametrize('get_available_pets', ["pupo", "pajaro"], indirect=True)
def test_find_available_pet_and_place_order(get_available_pets):
    resp, status_code = get_available_pets("pupo", "pajaro")
    print(resp, status_code)
    assert resp == []
    assert status_code == 200


