import grpc

import RegistrationService_pb2 as registr_data
import RegistrationService_pb2_grpc as registr_grpc

import common_pb2 as common_data
from utils.urls import SERVICE_URLS
from utils.randomather import client_data


class Client(object):

    def __init__(self, email=None, password=None):
        self.default_data = client_data()
        self.email = email or self.default_data['email']
        self.password = password or self.default_data['password']
        self.locale = 'en_GB'

    def create_client(self):
        request = registr_data.RegisterClientByEmailRequest(
            email=self.email,
            password=self.password,
            common_fields=common_data.CommonFields(
                locale=self.locale
            )
        )

        with grpc.insecure_channel(SERVICE_URLS['registration_service']) as chanel:
            stub = registr_grpc.RegistrationServiceStub(chanel)
            stub.RegisterClientByEmail(request, metadata=[
                ("x-real-ip", "127.0.0.1")
            ])

        print(self.email, self.password)

        return {
            'email': self.email,
            'password': self.password
        }


# new_client = Client(email='d.stepanishchenko+33@egt-ua.com', password='asdasd33')
# response = new_client.create_client()
# print(response)
