import requests
from Urls import Url, Endpoints
from faker import Faker

fake = Faker("ru_RU")


def register_new_user_and_return_login_password():
    login_pass = []
    email = fake.ascii_free_email()
    password = fake.password()
    user_name = fake.first_name()
    payload = {
        "email": email,
        "password": password,
        "name": user_name
    }
    response = requests.post(f'{Url.URL}{Endpoints.USER_REGISTRATION}', data=payload)
    if response.status_code == 200:
        login_pass.append(email)
        login_pass.append(password)
        login_pass.append(user_name)
    return login_pass, response
