import pytest


@pytest.fixture(name="testapp")
def fixture_testapp():
    from ...app import create_app

    app = create_app()
    yield app


@pytest.fixture(name="client")
def fixture_client(testapp):
    return testapp.test_client()
