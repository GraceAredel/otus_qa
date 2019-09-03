import requests


def test_answer(url_param):
    """test to check the status code from url through addoption"""
    response = requests.get(url_param)
    print(response.status_code)
    if url_param == "ya.ru":
        assert response.status_code == 200
    elif url_param == "gcdcdoogle.com":
        print("GOOOGLE!")
    else:
        print("DuckDuckGOOOOO")
