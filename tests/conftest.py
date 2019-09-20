import pytest
from Client.Client import Client


@pytest.yield_fixture(scope='function')
def create_client_by_grpc():
    client = Client()
    yield client.create_client()
