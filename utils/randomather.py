import random
import string


def client_data():
    return {
        'email': "egetishka.ukrainka+" + str(random.randint(0, 10000)) + random.choice(
            string.ascii_letters.lower()) + str(random.randint(0, 100)) + "@gmail.com",
        'password': '123qwe'
    }
