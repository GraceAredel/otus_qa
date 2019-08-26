import pytest
import math

from urllib import request
from bs4 import BeautifulSoup


def test_multiply():
    """here we test some math functions"""
    a = 5
    b = 10
    assert a * b == 50


def test_len():
    """here we test assering the len of a tuple"""
    t = (1, 2, 3, 4, 5)
    assert (len(t)) == 5


def test_isnan():
    """test if a number or a text provided is NaN"""
    num = 10
    if math.isnan(num):
        print("failed")
        pytest.fail()
    else:
        print("everything is okay")


def test_pi():
    """simple test to check math.pi func"""
    assert math.pi == 3.141592653589793


def test_title():
    url = 'http://www.google.com'
    html = request.urlopen(url).read().decode('utf-8')
    # html[:60]

    soup = BeautifulSoup(html, 'html.parser')
    title = soup.find('title')
    print(title)
    assert title.string == 'Google'


def test_reverse():
    """reversing function test"""
    l = [1, 2, 3, 4, 5]
    lr = reversed(l)
    assert list(lr) == [5, 4, 3, 2, 1]


def test_set():
    """test checks the set function"""
    words = ['hello', 'mother', 'father', 'hello']
    new_words = set(words)
    assert new_words == {'hello', 'mother', 'father'}


def capital_case(x):
    return x.capitalize()


def test_capital_case():
    """here we have a test with a method already declared"""
    assert capital_case('semaphore') == 'Semaphore'


def test_dict_value():
    """asserting an element value from the dict"""
    my_dict = {1: 'a', 2: 'b', 3: 'c'}
    assert my_dict[1] == 'a'


def test_greater_equal():
    """another simple test to check if the number is greater or equal to a given number"""
    num = 100
    assert num >= 100
