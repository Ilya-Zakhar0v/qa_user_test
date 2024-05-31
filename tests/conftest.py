import pytest


@pytest.fixture(scope='function')
def user_name(request):
    request.cls.user_name = "user1"

