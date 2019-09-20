from driver_config import get_driver
from Auth.Login import do_login


def test_create_client(create_client_by_grpc):
    client_data = create_client_by_grpc

    driver = get_driver()
    do_login(driver, client_data['email'], client_data['password'])
