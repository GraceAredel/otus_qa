import json
import pytest
import requests
import jsonpath


def basic_url():
    """defines the basic url we send"""
    url = "https://reqres.in"
    return url


def test_get_response():
    """this is a basic test for getting a response and asserting its 200"""
    response = requests.get('https://reqres.in/api/users?page=2')
    print(response)
    assert response.status_code == 200


def test_check_type_of_content():
    """checking the type of an id"""
    response = requests.get(basic_url() + '/api/users?page=2')
    json_response = json.loads(response.text)
    print(json_response)
    total_pages = jsonpath.jsonpath(json_response, 'total_pages')
    print(total_pages)
    assert isinstance(total_pages[0], int)


def test_create_new_user_using_json_file():
    """basic test for a POST request = create a new user and assert it was created"""
    with open("new_user.json") as file:
        json_input = file.read()
    request_json = json.loads(json_input)
    response = requests.post(basic_url() + '/api/users', request_json)
    print(response.content)
    assert response.status_code == 201
    response_json = json.loads(response.text)  # here we parse the response to a json format
    user_id = jsonpath.jsonpath(response_json, 'id')
    print(user_id[0])
    assert user_id != ''


DATA = [("michael.lawson@reqres.in", "1234"),
        ("eve.holt@reqres.in", "123456"),
        ("tobias.funke@reqres.in", "12345678")]


@pytest.mark.parametrize("email, password", DATA)
def test_register_new_user_parametrized(email, password):
    """try to register a few users using pytest.mark.parametrize"""
    response = requests.post(basic_url() + '/api/register',
                             data={"email": email, "password": password})
    print(response.content)
    assert response.status_code == 200


@pytest.mark.parametrize("name", ["username1, username2, username3"])
@pytest.mark.parametrize("job", ["job1, job2, job3"])
def test_reg_params(name, job):
    """register a new user using mark.parametrize"""
    response = requests.post(basic_url() + '/api/users', data={"name": name, "job": job})
    print(response.content)
    assert response.status_code == 201
