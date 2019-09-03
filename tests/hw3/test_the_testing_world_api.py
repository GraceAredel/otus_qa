import json
import pytest
import requests
import jsonpath

base_url = "http://thetestingworldapi.com"


def test_add_new_user():
    """basic test for adding a new user and asserting it was created"""
    f = open("C:\\Users\\grace\\PycharmProjects\\otus_qa\\tests\\hw3\\new_user_data.json", 'r')
    request_json = json.loads(f.read())
    response = requests.post(base_url + '/api/studentsDetails', request_json)
    print(response.text)
    student_id = jsonpath.jsonpath(response.json(), 'id')
    print(student_id[0])
    assert student_id[0] != ''


def test_tech_skills():
    """basic test of posting a json with some tech skills"""
    f = open("C:\\Users\\grace\\PycharmProjects\\otus_qa\\tests\\hw3\\tech_skills.json", 'r')
    request_json = json.loads(f.read())
    response = requests.post(base_url + '/api/technicalskills', request_json)
    print(response.text)
    assert response.status_code == 200


DATA = [("first1", "middle1", "last1", "01.01.1970"),
        ("first2", "middle2", "second2", "02.02.1970"),
        ("first3", "middle3", "second3", "03.03.1970")]


@pytest.mark.parametrize('first_name, middle_name, last_name, date_of_birth', DATA)
def test_create_users(first_name, middle_name, last_name, date_of_birth):
    """try to create a few users using parametrization"""
    response = requests.post(base_url + '/api/Students')
    print(response.content)
    assert response.status_code == 200
    response_json = json.loads(response.text)
    student_id = jsonpath.jsonpath(response_json, 'id')
    print(student_id[0, 1, 2])
    assert student_id[0, 1, 2] != ''
