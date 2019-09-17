"""basic test to check status code from given url"""
import requests


def test_answer(url_param):
    """test to check the status code from url through addoption"""
    response = requests.get(url_param)
    assert response.status_code == 200
