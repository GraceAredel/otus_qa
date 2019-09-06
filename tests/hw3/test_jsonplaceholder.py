"""API tests for a jsonplaceholder.typicode.com website"""
import json
import pytest
import requests
import jsonpath

BASE_URL = "https://jsonplaceholder.typicode.com"


def test_get_post_info():
    """get a user information and assert we got something"""
    response = requests.get(BASE_URL + "/posts/1")
    assert response.status_code == 200
    response_json = json.loads(response.text)
    user_id = jsonpath.jsonpath(response_json, 'userId')
    title = jsonpath.jsonpath(response_json, 'title')
    assert user_id[0] == 1
    assert title[0] == "sunt aut facere repellat provident occaecati excepturi optio reprehenderit"


def test_update_a_resource():
    """update the resource with an id=1 usin the json formatted data"""
    headers = {"Content-type": "application/json, charset=UTF-8"}
    data = {
        "id": 1,
        "title": 'foo',
        "body": 'bar',
        "userId": 1
    }
    response = requests.put(BASE_URL + '/posts/1', json=json.dumps(data), headers=headers)
    print(response.text)
    assert response.status_code == 200


@pytest.mark.parametrize("post_id", [1, 2, 3])
@pytest.mark.parametrize("title", ["foo, test, title"])
@pytest.mark.parametrize("body", ["bar, test2, body"])
@pytest.mark.parametrize("user_id", [1, 2, 3])
def test_create_posts(post_id, body, title, user_id):
    """parametrized test to create a few posts"""
    headers = {"Content-type": "application/json, charset=UTF-8"}
    response = requests.post(BASE_URL + '/posts',
                             data={"id": post_id, "title": title, "body": body,
                                   "userId": user_id}, headers=headers)
    print(response.text)
    post_id = jsonpath.jsonpath(response.json(), 'id')
    assert response.status_code == 201
    assert post_id[0] == 101
