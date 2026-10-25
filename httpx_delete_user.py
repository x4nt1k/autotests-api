import httpx
from tools.fakers import fake

URL = 'http://localhost:8000'
endpoint_create_user = '/api/v1/users'
endpoint_get_users = '/api/v1/users/'
endpoint_auth_user = '/api/v1/authentication/login'
endpoint_delete_users = '/api/v1/users/'
endpoint_patch_users = '/api/v1/users/'

create_users_payload = {
    "email": fake.email(),
    "password": "string",
    "lastName": "Petrovich",
    "firstName": "Ivanov",
    "middleName": "Petr"
}

response = httpx.post(url=URL + endpoint_create_user, json=create_users_payload)
print(response.status_code)
print(response.json())
user_id = response.json()["user"]["id"]
print("USER_ID: " + user_id)


auth_payload = {
    "email": create_users_payload["email"],
    "password": create_users_payload["password"]
}
response_auth = httpx.post(url=URL + endpoint_auth_user, json=auth_payload)
print(response_auth.status_code)
print(response_auth.json())
access_token = response_auth.json()['token']['accessToken']
headers = {"Authorization": f"Bearer {access_token}"}

print("Проверка пользака")
response_get_user = httpx.get(url=f'{URL}{endpoint_get_users}{user_id}', headers=headers)
print(response_get_user.status_code)
print(response_get_user.json())

patch_payload = {
    "email": fake.email(),
    "lastName": "string",
    "firstName": "string",
    "middleName": "string"
}
respone_patch = httpx.patch(url=f'{URL}{endpoint_patch_users}{user_id}', headers=headers, json=patch_payload)
print(respone_patch.status_code)
print(respone_patch.json())  

response_delete = httpx.delete(url=f'{URL}{endpoint_delete_users}{user_id}', headers=headers)
print(response_delete.status_code)
print(response_delete.json())


response_get_user = httpx.get(url=f'{URL}{endpoint_get_users}{user_id}', headers=headers)
print(response_get_user.status_code)
print(response_get_user.json())