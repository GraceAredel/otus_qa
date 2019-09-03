import pytest


def setup():
    print("basic setup into module")


def teardown():
    print("basic teardown into module")


@pytest.fixture(scope='session')
def hello_session():
    print('start session')
    yield
    print('end session')


@pytest.fixture(scope='module')
def hello_module():
    print('start tests for module')
    yield
    print('end tests for module')


@pytest.fixture(scope='class')
def hello_class():
    print('start tests for class')
    yield
    print('end tests for class')


@pytest.fixture(scope='function')
def hello_function():
    print('this is a last fixture')
    yield
    print('end tests for a function')


@pytest.fixture(scope="session", autouse=True)
def auto_session_resource(request):
    """ auto session resource fixture
    """
    print("auto_session_resource_setup")

    def auto_session_resource_teardown():
        print("auto_session_resource_teardown")
    request.addfinalizer(auto_session_resource_teardown)